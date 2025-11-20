"""
Custom Supabase Storage Backend for Django
Permet de stocker les fichiers media sur Supabase Storage
"""
from django.core.files.storage import Storage
from django.conf import settings
from supabase import create_client
from django.core.files.base import ContentFile
import os
from urllib.parse import urljoin


class SupabaseStorage(Storage):
    """
    Custom storage backend pour Supabase Storage
    """
    
    def __init__(self):
        self.supabase_url = settings.SUPABASE_URL
        self.supabase_key = settings.SUPABASE_KEY
        self.bucket_name = settings.SUPABASE_BUCKET
        
        # Initialiser le client Supabase
        self.client = create_client(self.supabase_url, self.supabase_key)
        
    def _open(self, name, mode='rb'):
        """
        Récupère un fichier depuis Supabase Storage
        """
        try:
            response = self.client.storage.from_(self.bucket_name).download(name)
            return ContentFile(response)
        except Exception as e:
            raise IOError(f"Erreur lors de l'ouverture du fichier {name}: {str(e)}")
    
    def _save(self, name, content):
        """
        Sauvegarde un fichier sur Supabase Storage
        """
        try:
            # Lire le contenu du fichier
            content.seek(0)
            file_data = content.read()
            
            # Upload sur Supabase
            self.client.storage.from_(self.bucket_name).upload(
                path=name,
                file=file_data,
                file_options={"content-type": self._guess_content_type(name)}
            )
            
            return name
        except Exception as e:
            # Si le fichier existe déjà, le mettre à jour
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
                raise IOError(f"Erreur lors de la sauvegarde du fichier {name}: {str(e)}, {str(update_error)}")
    
    def exists(self, name):
        """
        Vérifie si un fichier existe dans Supabase Storage
        """
        try:
            files = self.client.storage.from_(self.bucket_name).list(path=os.path.dirname(name))
            filename = os.path.basename(name)
            return any(f['name'] == filename for f in files)
        except:
            return False
    
    def delete(self, name):
        """
        Supprime un fichier de Supabase Storage
        """
        try:
            self.client.storage.from_(self.bucket_name).remove([name])
        except Exception as e:
            print(f"Erreur lors de la suppression du fichier {name}: {str(e)}")
    
    def url(self, name):
        """
        Retourne l'URL publique du fichier
        """
        try:
            # Obtenir l'URL publique
            response = self.client.storage.from_(self.bucket_name).get_public_url(name)
            return response
        except Exception as e:
            print(f"Erreur lors de la récupération de l'URL pour {name}: {str(e)}")
            return None
    
    def size(self, name):
        """
        Retourne la taille du fichier en bytes
        """
        try:
            files = self.client.storage.from_(self.bucket_name).list(path=os.path.dirname(name))
            filename = os.path.basename(name)
            for f in files:
                if f['name'] == filename:
                    return f.get('metadata', {}).get('size', 0)
            return 0
        except:
            return 0
    
    def _guess_content_type(self, name):
        """
        Devine le type MIME du fichier basé sur son extension
        """
        import mimetypes
        content_type, _ = mimetypes.guess_type(name)
        return content_type or 'application/octet-stream'
