from django.core.management.base import BaseCommand
from sicmi_app.models import TeamMember

class Command(BaseCommand):
    help = 'Popola il database con i membri del team SICMI'

    def handle(self, *args, **kwargs):
        # Cancella membri esistenti
        TeamMember.objects.all().delete()
        
        team_members = [
            # Ingegneri
            {
                'name': 'Ingénieur Construction 1',
                'position': 'Ingénieur',
                'specialization': 'Spécialisé en travaux de construction',
                'order': 1
            },
            {
                'name': 'Ingénieur Construction 2',
                'position': 'Ingénieur',
                'specialization': 'Spécialisé en travaux de construction',
                'order': 2
            },
            {
                'name': 'Ingénieur Maintenance',
                'position': 'Ingénieur',
                'specialization': 'Spécialisé en travaux de maintenance',
                'order': 3
            },
            
            # Spécialistes Qualité
            {
                'name': 'Spécialiste QHSE',
                'position': 'Spécialiste Qualité & Sécurité',
                'specialization': 'Aspects qualité et sécurité',
                'order': 4
            },
            {
                'name': 'Spécialiste QA/QC',
                'position': 'Contrôle Qualité',
                'specialization': 'Quality Assurance / Quality Control',
                'order': 5
            },
            
            # Préparateurs
            {
                'name': 'Préparateur Travaux 1',
                'position': 'Préparateur de Travaux',
                'specialization': 'Relevés sur site et plans de fabrication',
                'order': 6
            },
            {
                'name': 'Préparateur Travaux 2',
                'position': 'Préparateur de Travaux',
                'specialization': 'Relevés sur site et plans de fabrication',
                'order': 7
            },
            
            # Techniciens Chaudronnerie
            {
                'name': 'Technicien Chaudronnerie 1',
                'position': 'Technicien Chaudronnier',
                'specialization': 'Ouvrages chaudronnés et installation équipements',
                'order': 8
            },
            {
                'name': 'Technicien Chaudronnerie 2',
                'position': 'Technicien Chaudronnier',
                'specialization': 'Ouvrages chaudronnés et installation équipements',
                'order': 9
            },
            {
                'name': 'Technicien Chaudronnerie 3',
                'position': 'Technicien Chaudronnier',
                'specialization': 'Ouvrages chaudronnés et installation équipements',
                'order': 10
            },
            {
                'name': 'Technicien Chaudronnerie 4',
                'position': 'Technicien Chaudronnier',
                'specialization': 'Ouvrages chaudronnés et installation équipements',
                'order': 11
            },
            {
                'name': 'Technicien Chaudronnerie 5',
                'position': 'Technicien Chaudronnier',
                'specialization': 'Ouvrages chaudronnés et installation équipements',
                'order': 12
            },
            
            # Techniciens Tuyauterie
            {
                'name': 'Technicien Tuyauterie 1',
                'position': 'Technicien Tuyauteur',
                'specialization': 'Tuyauterie industrielle',
                'order': 13
            },
            {
                'name': 'Technicien Tuyauterie 2',
                'position': 'Technicien Tuyauteur',
                'specialization': 'Tuyauterie industrielle',
                'order': 14
            },
            {
                'name': 'Technicien Tuyauterie 3',
                'position': 'Technicien Tuyauteur',
                'specialization': 'Tuyauterie industrielle',
                'order': 15
            },
            
            # Technicien Maintenance
            {
                'name': 'Technicien Maintenance',
                'position': 'Technicien',
                'specialization': 'Maintenance industrielle',
                'order': 16
            },
            
            # Soudeurs Groupe 1
            {
                'name': 'Soudeur Expérimenté 1',
                'position': 'Soudeur Certifié',
                'specialization': 'Procédés 141, 111, 135 homologués',
                'order': 17
            },
            {
                'name': 'Soudeur Expérimenté 2',
                'position': 'Soudeur Certifié',
                'specialization': 'Procédés 141, 111, 135 homologués',
                'order': 18
            },
            {
                'name': 'Soudeur Expérimenté 3',
                'position': 'Soudeur Certifié',
                'specialization': 'Procédés 141, 111, 135 homologués',
                'order': 19
            },
            
            # Soudeurs Groupe 2
            {
                'name': 'Soudeur Certifié 1',
                'position': 'Soudeur',
                'specialization': 'Procédés 111, 141 homologués',
                'order': 20
            },
            {
                'name': 'Soudeur Certifié 2',
                'position': 'Soudeur',
                'specialization': 'Procédés 111, 141 homologués',
                'order': 21
            },
            {
                'name': 'Soudeur Certifié 3',
                'position': 'Soudeur',
                'specialization': 'Procédés 111, 141 homologués',
                'order': 22
            },
            {
                'name': 'Soudeur Certifié 4',
                'position': 'Soudeur',
                'specialization': 'Procédés 111, 141 homologués',
                'order': 23
            },
            
            # Techniciens Traitement de Surface
            {
                'name': 'Technicien Traitement Surface 1',
                'position': 'Technicien',
                'specialization': 'Traitement des surfaces métalliques',
                'order': 24
            },
            {
                'name': 'Technicien Traitement Surface 2',
                'position': 'Technicien',
                'specialization': 'Traitement des surfaces métalliques',
                'order': 25
            },
            {
                'name': 'Technicien Traitement Surface 3',
                'position': 'Technicien',
                'specialization': 'Traitement des surfaces métalliques',
                'order': 26
            },
            
            # Peintres
            {
                'name': 'Peintre Bâtiment 1',
                'position': 'Peintre',
                'specialization': 'Peinture en bâtiment',
                'order': 27
            },
            {
                'name': 'Peintre Bâtiment 2',
                'position': 'Peintre',
                'specialization': 'Peinture en bâtiment',
                'order': 28
            },
            {
                'name': 'Peintre Bâtiment 3',
                'position': 'Peintre',
                'specialization': 'Peinture en bâtiment',
                'order': 29
            },
            {
                'name': 'Peintre Bâtiment 4',
                'position': 'Peintre',
                'specialization': 'Peinture en bâtiment',
                'order': 30
            },
            
            # Techniciens Revêtements
            {
                'name': 'Technicien Revêtements 1',
                'position': 'Technicien',
                'specialization': 'Pose revêtements Equiton et Alucobond',
                'order': 31
            },
            {
                'name': 'Technicien Revêtements 2',
                'position': 'Technicien',
                'specialization': 'Pose revêtements Equiton et Alucobond',
                'order': 32
            },
            
            # Menuisiers Aluminium
            {
                'name': 'Menuisier Aluminium 1',
                'position': 'Menuisier',
                'specialization': 'Menuiserie aluminium',
                'order': 33
            },
            {
                'name': 'Menuisier Aluminium 2',
                'position': 'Menuisier',
                'specialization': 'Menuiserie aluminium',
                'order': 34
            },
            
            # Menuisier Bois
            {
                'name': 'Menuisier Bois',
                'position': 'Menuisier',
                'specialization': 'Menuiserie bois',
                'order': 35
            },
            
            # Serrurier
            {
                'name': 'Technicien Serrurier',
                'position': 'Serrurier',
                'specialization': 'Serrurerie métallique',
                'order': 36
            },
            
            # Technicien Échafaudage
            {
                'name': 'Technicien Échafaudage',
                'position': 'Technicien',
                'specialization': 'Montage et vérification échafaudage',
                'order': 37
            },
        ]
        
        created_count = 0
        for member_data in team_members:
            member, created = TeamMember.objects.get_or_create(
                name=member_data['name'],
                defaults=member_data
            )
            if created:
                created_count += 1
                self.stdout.write(self.style.SUCCESS(f'✓ Créé: {member.name} - {member.position}'))
            else:
                self.stdout.write(self.style.WARNING(f'→ Existe déjà: {member.name}'))
        
        total = TeamMember.objects.count()
        self.stdout.write(self.style.SUCCESS(f'\n✅ Total membres créés: {created_count}/{total}'))
        self.stdout.write(self.style.SUCCESS(f'\n📋 Composition de l\'équipe:'))
        self.stdout.write(self.style.SUCCESS(f'   - 3 Ingénieurs'))
        self.stdout.write(self.style.SUCCESS(f'   - 2 Spécialistes Qualité'))
        self.stdout.write(self.style.SUCCESS(f'   - 2 Préparateurs'))
        self.stdout.write(self.style.SUCCESS(f'   - 5 Techniciens Chaudronniers'))
        self.stdout.write(self.style.SUCCESS(f'   - 3 Techniciens Tuyauteurs'))
        self.stdout.write(self.style.SUCCESS(f'   - 7 Soudeurs Certifiés'))
        self.stdout.write(self.style.SUCCESS(f'   - 3 Techniciens Traitement Surface'))
        self.stdout.write(self.style.SUCCESS(f'   - 4 Peintres'))
        self.stdout.write(self.style.SUCCESS(f'   - 2 Techniciens Revêtements'))
        self.stdout.write(self.style.SUCCESS(f'   - 2 Menuisiers Aluminium'))
        self.stdout.write(self.style.SUCCESS(f'   - 1 Menuisier Bois'))
        self.stdout.write(self.style.SUCCESS(f'   - 1 Serrurier'))
        self.stdout.write(self.style.SUCCESS(f'   - 1 Technicien Échafaudage'))
