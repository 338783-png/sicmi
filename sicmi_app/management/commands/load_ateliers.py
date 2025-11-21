from django.core.management.base import BaseCommand
from sicmi_app.models import Atelier, AtelierImage
from pathlib import Path

class Command(BaseCommand):
    help = 'Charge les ateliers avec descriptions marketing'

    def handle(self, *args, **options):
        # Données des ateliers avec descriptions marketing
        ateliers_data = [
            {
                'name': "Atelier d'Assemblage",
                'description': """Notre atelier d'assemblage moderne est équipé pour réaliser des structures métalliques complexes avec précision. 
                Nos équipes spécialisées maîtrisent l'assemblage de charpentes métalliques, de structures industrielles et d'équipements sur mesure.
                
                ✓ Surface de 500m² dédiée à l'assemblage
                ✓ Équipements de levage et de manutention performants
                ✓ Contrôle qualité à chaque étape
                ✓ Respect strict des plans et tolérances""",
                'order': 1
            },
            {
                'name': "Atelier d'Usinage",
                'description': """Atelier d'usinage de précision équipé de machines-outils modernes pour tous vos besoins de fabrication métallique.
                Nous réalisons des pièces sur mesure avec une précision au micron près.
                
                ✓ Machines-outils à commande numérique
                ✓ Usinage de précision (tournage, fraisage, perçage)
                ✓ Capacité de production pour petites et grandes séries
                ✓ Contrôle dimensionnel rigoureux
                ✓ Traçabilité complète des pièces""",
                'order': 2
            },
            {
                'name': "Atelier de Production",
                'description': """Notre atelier de production intégré permet la fabrication complète de vos équipements industriels.
                De la découpe à la finition, nous maîtrisons toute la chaîne de production.
                
                ✓ Chaudronnerie et tuyauterie industrielle
                ✓ Soudage certifié (procédés 111, 141, 135)
                ✓ Traitement de surface et peinture industrielle
                ✓ Capacité de production élevée
                ✓ Respect des normes et codes en vigueur""",
                'order': 3
            },
            {
                'name': "Équipements & Machines",
                'description': """Parc d'équipements moderne et performant pour garantir la qualité et l'efficacité de nos prestations.
                Nos investissements constants en matériel nous permettent de rester à la pointe de la technologie.
                
                ✓ Nacelles et engins de levage
                ✓ Postes à souder dernière génération
                ✓ Machines-outils de précision
                ✓ Équipements de contrôle qualité (Elcometer)
                ✓ Sableuse professionnelle
                ✓ Maintenance préventive régulière de tous les équipements""",
                'order': 4
            }
        ]
        
        created_ateliers = 0
        
        for atelier_data in ateliers_data:
            # Créer ou récupérer l'atelier
            atelier, created = Atelier.objects.get_or_create(
                name=atelier_data['name'],
                defaults={
                    'description': atelier_data['description'],
                    'order': atelier_data['order']
                }
            )
            
            if created:
                created_ateliers += 1
                self.stdout.write(self.style.SUCCESS(f'✓ Créé: {atelier.name}'))
            else:
                # Mettre à jour la description
                atelier.description = atelier_data['description']
                atelier.order = atelier_data['order']
                atelier.save()
                self.stdout.write(self.style.WARNING(f'○ Mis à jour: {atelier.name}'))
        
        self.stdout.write(self.style.SUCCESS(f'\n✅ Résumé:'))
        self.stdout.write(self.style.SUCCESS(f'   • {created_ateliers} ateliers créés'))
        self.stdout.write(self.style.SUCCESS(f'📊 Total: {Atelier.objects.count()} ateliers'))
        self.stdout.write(self.style.WARNING(f'\n⚠️  Les images doivent être uploadées manuellement via l\'admin Django'))
        self.stdout.write(self.style.WARNING(f'   URL: https://sicmi-site.onrender.com/admin/sicmi_app/atelier/'))
