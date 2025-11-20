from django.core.management.base import BaseCommand
from django.core.management import call_command
import os

class Command(BaseCommand):
    help = 'Charger les données initiales depuis data_backup.json'

    def handle(self, *args, **options):
        data_file = 'data_backup.json'
        
        if os.path.exists(data_file):
            self.stdout.write(self.style.SUCCESS(f'Chargement des données depuis {data_file}...'))
            try:
                call_command('loaddata', data_file)
                self.stdout.write(self.style.SUCCESS('✅ Données chargées avec succès!'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'❌ Erreur lors du chargement: {e}'))
        else:
            self.stdout.write(self.style.WARNING(f'⚠️  Fichier {data_file} non trouvé. Ignoré.'))
