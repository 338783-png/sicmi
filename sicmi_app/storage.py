"""
Custom Supabase Storage Backend for Django
"""
import os
import mimetypes
from django.core.files.storage import Storage
from django.conf import settings
from supabase import create_client


class SupabaseStorage(Storage):
    """Custom storage backend for Supabase Storage"""
    
    def __init__(self):
        self.supabase_url = settings.SUPABASE_URL
        self.supabase_key = settings.SUPABASE_KEY
        self.bucket_name = settings.SUPABASE_BUCKET
        self.client = create_client(self.supabase_url, self.supabase_key)
    
    def _open(self, name, mode='rb'):
        """
        Retrieve a file from Supabase Storage
        """
        from django.core.files.base import ContentFile
        try:
            data = self.client.storage.from_(self.bucket_name).download(name)
            return ContentFile(data)
        except Exception as e:
            raise IOError(f"Error opening file {name}: {e}")
    
    def _save(self, name, content):
        """
        Save a file to Supabase Storage
        """
        try:
            # Read the file content
            content.seek(0)
            file_data = content.read()
            
            # Upload to Supabase
            self.client.storage.from_(self.bucket_name).upload(
                path=name,
                file=file_data,
                file_options={"content-type": self._guess_content_type(name)}
            )
            return name
        except Exception as e:
            # If upload fails (file exists), try update instead
            try:
                content.seek(0)
                file_data = content.read()
                self.client.storage.from_(self.bucket_name).update(
                    path=name,
                    file=file_data,
                    file_options={"content-type": self._guess_content_type(name)}
                )
                return name
            except Exception as update_error:
                raise IOError(f"Error saving {name}: {e}, {update_error}")
    
    def exists(self, name):
        """
        Check if a file exists in Supabase Storage
        """
        try:
            # List files in the bucket and check if our file exists
            path_parts = name.split('/')
            directory = '/'.join(path_parts[:-1]) if len(path_parts) > 1 else ''
            filename = path_parts[-1]
            
            files = self.client.storage.from_(self.bucket_name).list(path=directory)
            
            for file in files:
                if file['name'] == filename:
                    return True
            return False
        except Exception:
            return False
    
    def delete(self, name):
        """
        Delete a file from Supabase Storage
        """
        try:
            self.client.storage.from_(self.bucket_name).remove([name])
        except Exception as e:
            raise IOError(f"Error deleting {name}: {e}")
    
    def url(self, name):
        """
        Return the URL for accessing the file
        """
        try:
            return self.client.storage.from_(self.bucket_name).get_public_url(name)
        except Exception as e:
            raise IOError(f"Error getting URL for {name}: {e}")
    
    def size(self, name):
        """
        Return the size of a file in bytes
        """
        try:
            path_parts = name.split('/')
            directory = '/'.join(path_parts[:-1]) if len(path_parts) > 1 else ''
            filename = path_parts[-1]
            
            files = self.client.storage.from_(self.bucket_name).list(path=directory)
            
            for file in files:
                if file['name'] == filename:
                    return file.get('metadata', {}).get('size', 0)
            return 0
        except Exception:
            return 0
    
    def _guess_content_type(self, name):
        """
        Guess the content type of a file based on its name
        """
        content_type, _ = mimetypes.guess_type(name)
        return content_type or 'application/octet-stream'
