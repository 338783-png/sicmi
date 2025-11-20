from django.core.management.base import BaseCommand
from sicmi_app.models import Atelier, AtelierImage
import os
from django.conf import settings

class Command(BaseCommand):
    help = 'Populate ateliers with their images'

    def handle(self, *args, **kwargs):
        # Clear existing data
        AtelierImage.objects.all().delete()
        Atelier.objects.all().delete()
        
        self.stdout.write(self.style.SUCCESS('Cleared existing ateliers and images'))

        # Define ateliers structure matching the folders
        ateliers_data = [
            {
                'name': "Atelier d'assemblage",
                'description': "Notre atelier d'assemblage est équipé pour réaliser tous types de montages et d'assemblages de structures métalliques. Nous disposons d'un espace optimisé et d'équipements modernes pour garantir la précision et la qualité de chaque assemblage.",
                'order': 1,
                'images': ['atelier-production-charpente-metallique-bouquet.jpeg']
            },
            {
                'name': "Atelier d'usinage",
                'description': "Équipé de machines-outils de haute précision, notre atelier d'usinage permet la réalisation de pièces complexes avec une exactitude millimétrique. Nous maîtrisons l'ensemble des techniques d'usinage pour répondre aux exigences les plus strictes.",
                'order': 2,
                'images': ['1.jpg', 'OIP (2).webp', 'OIP (3).webp']
            },
            {
                'name': "Atelier de production",
                'description': "Notre atelier de production centralise l'ensemble des activités de fabrication. Organisé de manière optimale, il permet une production efficace tout en maintenant les plus hauts standards de qualité et de sécurité.",
                'order': 3,
                'images': ['2.jpg']
            },
            {
                'name': "Équipements & Machines",
                'description': "SICMI dispose d'un parc machines moderne et diversifié comprenant des équipements de pointe pour la chaudronnerie, la tuyauterie, le soudage et la maintenance industrielle. Notre investissement continu dans les technologies nous permet d'offrir des prestations de haute qualité.",
                'order': 4,
                'images': ['3.jpg', '4.jpg', '5.jpg', '6.jpg', '7.jpg', '8.jpg']
            }
        ]

        # Create ateliers and their images
        for atelier_data in ateliers_data:
            atelier = Atelier.objects.create(
                name=atelier_data['name'],
                description=atelier_data['description'],
                order=atelier_data['order']
            )
            
            self.stdout.write(self.style.SUCCESS(f'Created atelier: {atelier.name}'))
            
            # Create images for this atelier
            for idx, image_name in enumerate(atelier_data['images'], 1):
                # Construct the path matching the folder structure
                folder_name = atelier_data['name']
                image_path = f"images/Ateliers & Équipements/{folder_name}/{image_name}"
                
                AtelierImage.objects.create(
                    atelier=atelier,
                    image=image_path,
                    caption=f"{atelier.name} - Image {idx}",
                    order=idx
                )
                
                self.stdout.write(self.style.SUCCESS(f'  Added image: {image_name}'))

        self.stdout.write(self.style.SUCCESS('\nSuccessfully populated ateliers!'))
        self.stdout.write(self.style.SUCCESS(f'Total ateliers created: {Atelier.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'Total images created: {AtelierImage.objects.count()}'))
