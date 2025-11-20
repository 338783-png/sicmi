from django.core.files.storage import Storage
from django.core.files.base import ContentFile
from cloudinary import uploader
from cloudinary.utils import cloudinary_url
import cloudinary
import os


class CloudinaryStorage(Storage):
    """Custom Cloudinary storage backend that actually works"""
    
    def _save(self, name, content):
        """Save file to Cloudinary"""
        # Upload to Cloudinary
        result = uploader.upload(
            content,
            folder=os.path.dirname(name) if os.path.dirname(name) else None,
            public_id=os.path.splitext(os.path.basename(name))[0],
            resource_type='auto'
        )
        # Return the public_id with version
        return f"{result['public_id']}.{result['format']}"
    
    def _open(self, name, mode='rb'):
        """Not implemented - not needed for our use case"""
        raise NotImplementedError("CloudinaryStorage doesn't support opening files")
    
    def url(self, name):
        """Return the Cloudinary URL for the file"""
        # Si c'est déjà une URL complète, la retourner telle quelle
        if name.startswith('http'):
            return name
        
        # Supprimer l'extension du nom pour obtenir le public_id
        public_id = os.path.splitext(name)[0]
        
        # Générer l'URL Cloudinary
        url, options = cloudinary_url(public_id, secure=True)
        return url
    
    def exists(self, name):
        """Check if file exists - always return False to allow uploads"""
        return False
    
    def delete(self, name):
        """Delete file from Cloudinary"""
        public_id = os.path.splitext(name)[0]
        uploader.destroy(public_id)
    
    def size(self, name):
        """Return file size - not implemented"""
        return 0
