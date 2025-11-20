from django.core.management.base import BaseCommand, CommandError
from sicmi_app.models import Service
from django.conf import settings
import os


class Command(BaseCommand):
    help = 'Create a Service entry. Usage: python manage.py create_service --name "Nom" --category construction --description "..." [--image media/path.jpg]'

    def add_arguments(self, parser):
        parser.add_argument('--name', required=True, help='Service name')
        parser.add_argument('--category', required=True, help='Category slug (one of Service.CATEGORY_CHOICES keys)')
        parser.add_argument('--description', required=False, default='', help='Short description')
        parser.add_argument('--image', required=False, help='Path relative to MEDIA_ROOT for main_image (optional)')

    def handle(self, *args, **options):
        name = options['name']
        category = options['category']
        description = options['description']
        image = options.get('image')

        valid_categories = [c[0] for c in Service.CATEGORY_CHOICES]
        if category not in valid_categories:
            raise CommandError(f"Invalid category. Valid options: {', '.join(valid_categories)}")

        svc = Service(name=name, category=category, description=description)
        if image:
            # verify file exists under MEDIA_ROOT
            media_path = os.path.join(settings.MEDIA_ROOT, image)
            if not os.path.exists(media_path):
                raise CommandError(f"Image file not found at {media_path}")
            # assign path relative to upload_to
            svc.main_image.name = image

        svc.save()
        self.stdout.write(self.style.SUCCESS(f"Service créé: id={svc.id} name={svc.name} category={svc.category}"))
