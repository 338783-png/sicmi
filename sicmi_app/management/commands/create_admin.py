from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import os

class Command(BaseCommand):
    help = 'Créer un superutilisateur automatiquement'

    def handle(self, *args, **options):
        username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
        email = os.environ.get('DJANGO_SUPERUSER_EMAIL')
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')
        
        if not username or not email or not password:
            self.stdout.write(self.style.WARNING(
                'Variables d\'environnement manquantes: DJANGO_SUPERUSER_USERNAME, '
                'DJANGO_SUPERUSER_EMAIL, DJANGO_SUPERUSER_PASSWORD. '
                'Création du superutilisateur ignorée.'
            ))
            return
        
        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(
                username=username,
                email=email,
                password=password
            )
            self.stdout.write(self.style.SUCCESS(f'Superutilisateur "{username}" créé avec succès!'))
        else:
            self.stdout.write(self.style.WARNING(f'Le superutilisateur "{username}" existe déjà.'))
