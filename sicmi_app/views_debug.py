from django.http import JsonResponse
from django.conf import settings

def cloudinary_debug(request):
    """Vue de debug pour vérifier la configuration Cloudinary"""
    
    config = {
        'CLOUDINARY_CONFIGURED': bool(settings.CLOUDINARY_STORAGE.get('CLOUD_NAME')),
        'CLOUD_NAME': settings.CLOUDINARY_STORAGE.get('CLOUD_NAME', 'NOT_SET')[:10] + '...',
        'API_KEY': settings.CLOUDINARY_STORAGE.get('API_KEY', 'NOT_SET')[:5] + '...',
        'API_SECRET_SET': bool(settings.CLOUDINARY_STORAGE.get('API_SECRET')),
        'STORAGE_BACKEND': settings.STORAGES['default']['BACKEND'],
    }
    
    return JsonResponse(config)
