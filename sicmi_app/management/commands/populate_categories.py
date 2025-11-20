from django.core.management.base import BaseCommand
from sicmi_app.models import ServiceCategory

class Command(BaseCommand):
    help = 'Crée les catégories de service par défaut'

    def handle(self, *args, **kwargs):
        categories = [
            {
                'name': 'Constructions neuves et revamping',
                'slug': 'construction',
                'icon': 'fa-building',
                'description': 'Construction de structures métalliques, bâtiments industriels et revamping',
                'order': 1
            },
            {
                'name': 'Maintenance industrielle',
                'slug': 'maintenance',
                'icon': 'fa-tools',
                'description': 'Maintenance préventive et curative des équipements industriels',
                'order': 2
            },
            {
                'name': 'Accompagnement',
                'slug': 'accompagnement',
                'icon': 'fa-hands-helping',
                'description': 'Accompagnement technique et conseil en ingénierie',
                'order': 3
            },
            {
                'name': 'Travaux de Façade',
                'slug': 'facade',
                'icon': 'fa-home',
                'description': 'Installation et rénovation de façades et bardages',
                'order': 4
            },
            {
                'name': 'Travaux de rénovation',
                'slug': 'renovation',
                'icon': 'fa-paint-roller',
                'description': 'Rénovation et modernisation de structures existantes',
                'order': 5
            },
        ]
        
        for cat_data in categories:
            category, created = ServiceCategory.objects.get_or_create(
                slug=cat_data['slug'],
                defaults=cat_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'✓ Créée: {category.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'→ Existe déjà: {category.name}'))
        
        self.stdout.write(self.style.SUCCESS(f'\n✅ Total catégories: {ServiceCategory.objects.count()}'))
