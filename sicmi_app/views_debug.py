from django.http import HttpResponse
from django.conf import settings
import os

def cloudinary_debug(request):
    """View pour debugger la configuration Cloudinary"""
    
    html = """<!DOCTYPE html>
<html>
<head>
    <title>Cloudinary Debug</title>
    <style>
        body {{ font-family: monospace; padding: 20px; background: #f5f5f5; }}
        .section {{ background: white; padding: 20px; margin: 10px 0; border-radius: 5px; }}
        .ok {{ color: green; }}
        .error {{ color: red; }}
        pre {{ background: #f0f0f0; padding: 10px; overflow-x: auto; }}
    </style>
</head>
<body>
    <h1>🔍 Diagnostic Cloudinary</h1>
    
    <div class="section">
        <h2>1. Variables d'environnement</h2>
        <pre>CLOUDINARY_CLOUD_NAME: {cloud_name}</pre>
        <pre>CLOUDINARY_API_KEY: {api_key}</pre>
        <pre>CLOUDINARY_API_SECRET: {api_secret_masked}</pre>
    </div>
    
    <div class="section">
        <h2>2. Configuration Django</h2>
        <pre>DEFAULT_FILE_STORAGE: {default_storage}</pre>
        <pre>CLOUDINARY_STORAGE: {cloudinary_storage}</pre>
    </div>
    
    <div class="section">
        <h2>3. Test d'import</h2>
        <pre>{import_test}</pre>
    </div>
    
    <div class="section">
        <h2>4. Base de données</h2>
        <pre>{db_info}</pre>
    </div>
    
    <div class="section">
        <h2>5. Dernières images uploadées</h2>
        <pre>{recent_images}</pre>
    </div>
</body>
</html>"""
    
    # Variables d'environnement
    cloud_name = os.environ.get('CLOUDINARY_CLOUD_NAME', '❌ NON DÉFINI')
    api_key = os.environ.get('CLOUDINARY_API_KEY', '❌ NON DÉFINI')
    api_secret = os.environ.get('CLOUDINARY_API_SECRET', '❌ NON DÉFINI')
    api_secret_masked = api_secret[:5] + '****' if api_secret != '❌ NON DÉFINI' else api_secret
    
    # Configuration Django
    default_storage = settings.DEFAULT_FILE_STORAGE
    cloudinary_storage = str(settings.CLOUDINARY_STORAGE)
    
    # Test d'import
    try:
        import cloudinary
        import cloudinary_storage
        import_test = "✅ Modules cloudinary importés correctement"
    except ImportError as e:
        import_test = f"❌ Erreur d'import: {e}"
    
    # Base de données
    from sicmi_app.models import Service, Project, Atelier
    db_info = f"""
Services: {Service.objects.count()}
Projets: {Project.objects.count()}
Ateliers: {Atelier.objects.count()}
    """
    
    # Images récentes
    recent_images = ""
    try:
        services = Service.objects.filter(main_image__isnull=False)[:3]
        for s in services:
            recent_images += f"\n📦 Service '{s.name}':\n"
            recent_images += f"   Type: {type(s.main_image).__name__}\n"
            recent_images += f"   Chemin: {s.main_image.name if s.main_image else 'None'}\n"
            if hasattr(s.main_image, 'url'):
                recent_images += f"   URL: {s.main_image.url}\n"
        
        ateliers = Atelier.objects.all()[:3]
        for a in ateliers:
            images = a.images.all()
            if images:
                recent_images += f"\n🏭 Atelier '{a.name}':\n"
                for img in images[:2]:
                    recent_images += f"   Type: {type(img.image).__name__}\n"
                    recent_images += f"   Chemin: {img.image.name if img.image else 'None'}\n"
                    if hasattr(img.image, 'url'):
                        recent_images += f"   URL: {img.image.url}\n"
        
        if not recent_images:
            recent_images = "Aucune image trouvée dans la base de données"
    except Exception as e:
        recent_images = f"❌ Erreur: {e}"
    
    return HttpResponse(html.format(
        cloud_name=cloud_name,
        api_key=api_key,
        api_secret_masked=api_secret_masked,
        default_storage=default_storage,
        cloudinary_storage=cloudinary_storage,
        import_test=import_test,
        db_info=db_info,
        recent_images=recent_images
    ))
