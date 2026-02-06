from django.core.management.base import BaseCommand
from django.conf import settings
from sicmi_app.models import ServiceImage, ProjectImage, AtelierImage, TeamMember
import cloudinary.uploader
import os


class Command(BaseCommand):
    help = 'Migre les images locales vers Cloudinary'

    def add_arguments(self, parser):
        parser.add_argument(
            '--dry-run',
            action='store_true',
            help='Affiche ce qui serait migré sans effectuer de changements',
        )

    def handle(self, *args, **options):
        dry_run = options['dry_run']
        
        if dry_run:
            self.stdout.write(self.style.WARNING('🔍 Mode DRY-RUN - aucune modification ne sera effectuée\n'))
        
        self.stdout.write('🚀 Migration des images vers Cloudinary...\n')
        
        # Vérifier la configuration Cloudinary
        cloudinary_storage = getattr(settings, 'CLOUDINARY_STORAGE', {})
        cloud_name = cloudinary_storage.get('CLOUD_NAME', '')
        if not cloud_name:
            self.stdout.write(self.style.WARNING(
                '⚠️ Cloudinary non configuré - migration ignorée'
            ))
            return
        
        self.stdout.write(f'☁️ Cloudinary configuré: {cloud_name}\n')
        
        # Liste des modèles avec images
        models_with_images = [
            (ServiceImage, 'image', 'services'),
            (ProjectImage, 'image', 'projects'),
            (AtelierImage, 'image', 'ateliers'),
            (TeamMember, 'image', 'team'),
        ]
        
        total_migrated = 0
        total_skipped = 0
        total_errors = 0
        
        for model, field_name, folder in models_with_images:
            model_name = model.__name__
            self.stdout.write(f'\n📦 Traitement de {model_name}...')
            
            queryset = model.objects.all()
            if queryset.count() == 0:
                self.stdout.write(self.style.WARNING(f'  ⚠ Aucun enregistrement trouvé'))
                continue
            
            for obj in queryset:
                image_field = getattr(obj, field_name, None)
                
                # Vérifier si le champ image existe et a une valeur
                if not image_field:
                    self.stdout.write(f'  ⏭ {obj} - pas d\'image')
                    total_skipped += 1
                    continue
                
                try:
                    image_url = str(image_field.url) if image_field else ''
                    
                    # Vérifier si c'est déjà une URL Cloudinary
                    if 'cloudinary' in image_url or 'res.cloudinary.com' in image_url:
                        self.stdout.write(f'  ✓ {obj} - déjà sur Cloudinary')
                        total_skipped += 1
                        continue
                    
                    # Construire le chemin local
                    media_root = getattr(settings, 'MEDIA_ROOT', '')
                    if hasattr(image_field, 'path'):
                        local_path = image_field.path
                    else:
                        local_path = os.path.join(media_root, str(image_field))
                    
                    if not os.path.exists(local_path):
                        self.stdout.write(
                            self.style.WARNING(f'  ⚠ {obj} - fichier local introuvable: {local_path}')
                        )
                        total_errors += 1
                        continue
                    
                    if dry_run:
                        self.stdout.write(
                            self.style.SUCCESS(f'  📤 {obj} serait migré depuis: {local_path}')
                        )
                        total_migrated += 1
                    else:
                        # Upload vers Cloudinary
                        result = cloudinary.uploader.upload(
                            local_path,
                            folder=f"sicmi/{folder}",
                            resource_type="image",
                            overwrite=True,
                            invalidate=True
                        )
                        
                        # Mettre à jour le champ avec l'URL Cloudinary
                        new_value = result.get('public_id', '')
                        setattr(obj, field_name, new_value)
                        obj.save(update_fields=[field_name])
                        
                        self.stdout.write(
                            self.style.SUCCESS(f'  ✓ {obj} migré: {result["secure_url"][:60]}...')
                        )
                        total_migrated += 1
                        
                except Exception as e:
                    self.stdout.write(
                        self.style.ERROR(f'  ✗ {obj} - Erreur: {str(e)}')
                    )
                    total_errors += 1
        
        # Résumé
        self.stdout.write('\n' + '=' * 60)
        self.stdout.write(self.style.SUCCESS(f'✅ Images migrées: {total_migrated}'))
        self.stdout.write(f'⏭ Images ignorées (déjà sur Cloudinary ou vides): {total_skipped}')
        if total_errors > 0:
            self.stdout.write(self.style.ERROR(f'❌ Erreurs: {total_errors}'))
        
        if dry_run:
            self.stdout.write(self.style.WARNING(
                '\n💡 Exécutez sans --dry-run pour effectuer la migration'
            ))
