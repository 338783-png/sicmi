from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import os

class Command(BaseCommand):
    help = 'Créer un superutilisateur automatiquement'

    def handle(self, *args, **options):
        username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
        email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'jordanietane2@gmail.com')
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'Admin@SICMI2025')
        
        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(
                username=username,
                email=email,
                password=password
            )
            self.stdout.write(self.style.SUCCESS(f'Superutilisateur "{username}" créé avec succès!'))
        else:
            self.stdout.write(self.style.WARNING(f'Le superutilisateur "{username}" existe déjà.'))
