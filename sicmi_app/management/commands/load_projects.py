from django.core.management.base import BaseCommand
from django.core.files import File
from sicmi_app.models import Project, ProjectImage
from datetime import date
import os


class Command(BaseCommand):
    help = 'Charge les projets de démonstration'

    def handle(self, *args, **options):
        self.stdout.write('🚀 Chargement des projets...\n')

        # Données des projets
        projects_data = [
            {
                'title': 'Maintenance Bacs de Stockage SONARA',
                'client': 'SONARA - Société Nationale de Raffinage',
                'description': """Projet de maintenance préventive et corrective des bacs de stockage de la raffinerie SONARA à Limbé.

Travaux réalisés:
• Inspection complète de 12 bacs de stockage
• Réparation des fonds de bacs
• Remplacement des joints et vannes
• Traitement anticorrosion
• Tests d'étanchéité

Durée: 6 mois
Valeur du projet: Confidentiel

Ce projet a permis de prolonger la durée de vie des installations de stockage tout en garantissant la sécurité des opérations.""",
                'completion_date': date(2025, 6, 15),
            },
            {
                'title': 'Construction Passerelle Industrielle TRADEX',
                'client': 'TRADEX - Terminal et Raffinage',
                'description': """Construction et installation d'une passerelle métallique de liaison pour le dépôt pétrolier TRADEX.

Réalisations:
• Étude et conception de la structure
• Fabrication en atelier de 150m linéaires
• Installation sur site avec levage
• Pose des garde-corps et planchers
• Peinture anticorrosion

La passerelle permet un accès sécurisé aux différents équipements du site et facilite les opérations de maintenance.

Normes respectées: EN 1090, NF E 85-015""",
                'completion_date': date(2025, 3, 20),
            },
            {
                'title': 'Rénovation Tuyauterie Usine CIMENCAM',
                'client': 'CIMENCAM - Cimenteries du Cameroun',
                'description': """Projet de rénovation du réseau de tuyauterie de l'usine CIMENCAM de Douala.

Scope des travaux:
• Remplacement de 500m de tuyauterie acier carbone
• Installation de supports et colliers
• Soudage certifié ASME IX
• Tests hydrostatiques
• Isolation thermique

Notre équipe a travaillé en coordination avec les opérations pour minimiser les arrêts de production.

Durée du projet: 4 mois""",
                'completion_date': date(2024, 11, 10),
            },
            {
                'title': 'Fabrication Cuves Inox Brasseries',
                'client': 'SABC - Société Anonyme des Brasseries du Cameroun',
                'description': """Fabrication et installation de cuves en acier inoxydable pour la nouvelle ligne de production SABC.

Détails du projet:
• 4 cuves de fermentation de 50m³ chacune
• 2 cuves de stockage de 100m³
• Tuyauterie inox 304L associée
• Vannes et instrumentation
• Mise en service et tests

Toutes les soudures ont été réalisées selon les normes agroalimentaires avec contrôle radiographique.

Certification: ISO 22000 compatible""",
                'completion_date': date(2024, 8, 25),
            },
            {
                'title': 'Montage Structure Métallique Entrepôt',
                'client': 'BOLLORÉ Transport & Logistics',
                'description': """Construction d'un entrepôt logistique avec structure métallique complète.

Caractéristiques:
• Surface couverte: 2000m²
• Hauteur sous poutre: 8m
• Portée libre: 25m
• Bardage double peau avec isolation
• Portes sectionnelles automatiques

Le projet a été livré dans les délais malgré les contraintes logistiques du site portuaire.

Durée: 5 mois""",
                'completion_date': date(2025, 1, 30),
            },
            {
                'title': 'Revamping Installation Gaz PERENCO',
                'client': 'PERENCO Cameroon',
                'description': """Modernisation des installations de traitement de gaz du champ de Sanaga Sud.

Travaux effectués:
• Remplacement des échangeurs thermiques
• Installation de nouvelles vannes de régulation
• Mise à jour du système de sécurité
• Réfection des revêtements anticorrosion
• Modifications de la tuyauterie process

Ce projet a permis d'augmenter la capacité de production de 20% tout en améliorant la sécurité des installations.

Standards: ASME, API, NORSOK""",
                'completion_date': date(2024, 5, 12),
            },
        ]

        projects_created = 0

        for project_data in projects_data:
            project, created = Project.objects.get_or_create(
                title=project_data['title'],
                defaults={
                    'client': project_data['client'],
                    'description': project_data['description'],
                    'completion_date': project_data['completion_date'],
                    'main_image': '',  # Sera ajouté via admin ou Cloudinary
                }
            )

            if created:
                projects_created += 1
                self.stdout.write(
                    self.style.SUCCESS(f'  ✓ Projet créé: {project.title}')
                )
            else:
                # Mettre à jour les informations
                project.client = project_data['client']
                project.description = project_data['description']
                project.completion_date = project_data['completion_date']
                project.save()
                self.stdout.write(f'  ↺ Projet mis à jour: {project.title}')

        self.stdout.write('\n' + '=' * 50)
        self.stdout.write(
            self.style.SUCCESS(f'✅ {projects_created} projets créés')
        )
        self.stdout.write(
            self.style.WARNING(
                '\n💡 N\'oubliez pas d\'ajouter les images via l\'admin Django!'
            )
        )
