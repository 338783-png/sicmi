from django.core.management.base import BaseCommand
from sicmi_app.models import TeamMember

class Command(BaseCommand):
    help = 'Charge les membres de l\'équipe technique SICMI'

    def handle(self, *args, **kwargs):
        # Supprimer les anciens membres si nécessaire
        # TeamMember.objects.all().delete()
        
        team_data = [
            # Ingénieurs (2 construction + 1 maintenance)
            {"name": "Ingénieur Construction 1", "position": "Ingénieur", "specialization": "Travaux de construction", "order": 1},
            {"name": "Ingénieur Construction 2", "position": "Ingénieur", "specialization": "Travaux de construction", "order": 2},
            {"name": "Ingénieur Maintenance", "position": "Ingénieur", "specialization": "Travaux de maintenance industrielle", "order": 3},
            
            # Spécialistes Qualité & Sécurité
            {"name": "Spécialiste QHSE", "position": "Spécialiste", "specialization": "Qualité, Hygiène, Sécurité et Environnement", "order": 4},
            {"name": "Spécialiste QA/QC", "position": "Spécialiste", "specialization": "Assurance Qualité et Contrôle Qualité", "order": 5},
            
            # Préparateurs de travaux (2)
            {"name": "Préparateur Travaux 1", "position": "Préparateur", "specialization": "Relevés sur site et élaboration des plans de fabrication", "order": 6},
            {"name": "Préparateur Travaux 2", "position": "Préparateur", "specialization": "Relevés sur site et élaboration des plans de fabrication", "order": 7},
            
            # Techniciens chaudronnerie (5)
            {"name": "Technicien Chaudronnerie 1", "position": "Technicien", "specialization": "Ouvrages chaudronnés et installation d'équipements", "order": 8},
            {"name": "Technicien Chaudronnerie 2", "position": "Technicien", "specialization": "Ouvrages chaudronnés et installation d'équipements", "order": 9},
            {"name": "Technicien Chaudronnerie 3", "position": "Technicien", "specialization": "Ouvrages chaudronnés et installation d'équipements", "order": 10},
            {"name": "Technicien Chaudronnerie 4", "position": "Technicien", "specialization": "Ouvrages chaudronnés et installation d'équipements", "order": 11},
            {"name": "Technicien Chaudronnerie 5", "position": "Technicien", "specialization": "Ouvrages chaudronnés et installation d'équipements", "order": 12},
            
            # Techniciens tuyauterie (3)
            {"name": "Technicien Tuyauterie 1", "position": "Technicien", "specialization": "Tuyauterie industrielle", "order": 13},
            {"name": "Technicien Tuyauterie 2", "position": "Technicien", "specialization": "Tuyauterie industrielle", "order": 14},
            {"name": "Technicien Tuyauterie 3", "position": "Technicien", "specialization": "Tuyauterie industrielle", "order": 15},
            
            # Technicien maintenance
            {"name": "Technicien Maintenance", "position": "Technicien", "specialization": "Maintenance industrielle", "order": 16},
            
            # Soudeurs homologués procédés 141, 111, 135 (3)
            {"name": "Soudeur 1", "position": "Soudeur", "specialization": "Procédés 141, 111, 135 - Homologué et expérimenté", "order": 17},
            {"name": "Soudeur 2", "position": "Soudeur", "specialization": "Procédés 141, 111 - Homologué et expérimenté", "order": 18},
            {"name": "Soudeur 3", "position": "Soudeur", "specialization": "Procédés 141, 111 - Homologué et expérimenté", "order": 19},
            
            # Soudeurs homologués procédés 111, 141 (4)
            {"name": "Soudeur 4", "position": "Soudeur", "specialization": "Procédés 111, 141 - Homologué et expérimenté", "order": 20},
            {"name": "Soudeur 5", "position": "Soudeur", "specialization": "Procédés 111, 141 - Homologué et expérimenté", "order": 21},
            {"name": "Soudeur 6", "position": "Soudeur", "specialization": "Procédés 111, 141 - Homologué et expérimenté", "order": 22},
            {"name": "Soudeur 7", "position": "Soudeur", "specialization": "Procédés 111, 141 - Homologué et expérimenté", "order": 23},
            
            # Techniciens traitement surfaces (3)
            {"name": "Technicien Surfaces 1", "position": "Technicien", "specialization": "Traitement des surfaces métalliques", "order": 24},
            {"name": "Technicien Surfaces 2", "position": "Technicien", "specialization": "Traitement des surfaces métalliques", "order": 25},
            {"name": "Technicien Surfaces 3", "position": "Technicien", "specialization": "Traitement des surfaces métalliques", "order": 26},
            
            # Peintres bâtiment (4)
            {"name": "Peintre 1", "position": "Peintre", "specialization": "Peinture bâtiment", "order": 27},
            {"name": "Peintre 2", "position": "Peintre", "specialization": "Peinture bâtiment", "order": 28},
            {"name": "Peintre 3", "position": "Peintre", "specialization": "Peinture bâtiment", "order": 29},
            {"name": "Peintre 4", "position": "Peintre", "specialization": "Peinture bâtiment", "order": 30},
            
            # Techniciens revêtements (2)
            {"name": "Technicien Revêtements 1", "position": "Technicien", "specialization": "Pose de revêtements Equiton et Alucobond", "order": 31},
            {"name": "Technicien Revêtements 2", "position": "Technicien", "specialization": "Pose de revêtements Equiton et Alucobond", "order": 32},
            
            # Menuisiers (2 aluminium + 1 bois)
            {"name": "Menuisier Aluminium 1", "position": "Menuisier", "specialization": "Menuiserie aluminium", "order": 33},
            {"name": "Menuisier Aluminium 2", "position": "Menuisier", "specialization": "Menuiserie aluminium", "order": 34},
            {"name": "Menuisier Bois", "position": "Menuisier", "specialization": "Menuiserie bois", "order": 35},
            
            # Serrurier
            {"name": "Technicien Serrurier", "position": "Serrurier", "specialization": "Serrurerie métallique", "order": 36},
            
            # Échafaudage
            {"name": "Technicien Échafaudage", "position": "Technicien", "specialization": "Montage et vérification d'échafaudage", "order": 37},
        ]
        
        created_count = 0
        for data in team_data:
            member, created = TeamMember.objects.get_or_create(
                name=data['name'],
                defaults=data
            )
            if created:
                created_count += 1
                self.stdout.write(self.style.SUCCESS(f'✓ Créé: {member.name} - {member.specialization}'))
            else:
                self.stdout.write(self.style.WARNING(f'○ Existe déjà: {member.name}'))
        
        self.stdout.write(self.style.SUCCESS(f'\n✅ {created_count} membres ajoutés sur {len(team_data)} au total'))
        self.stdout.write(self.style.SUCCESS(f'📊 Total dans la base: {TeamMember.objects.count()} membres'))
