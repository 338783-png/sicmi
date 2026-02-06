from django.core.management.base import BaseCommand
from sicmi_app.models import ServiceCategory, Service


class Command(BaseCommand):
    help = 'Charge les services pour toutes les catégories'

    def handle(self, *args, **options):
        self.stdout.write('🚀 Chargement des services...\n')

        # Données des services par catégorie
        services_data = {
            'Maintenance industrielle': [
                {
                    'name': 'Maintenance préventive',
                    'description': """SICMI assure la maintenance préventive de vos installations industrielles pour garantir leur bon fonctionnement et prolonger leur durée de vie.

Nos prestations incluent:
• Inspection régulière des équipements
• Remplacement préventif des pièces d'usure
• Contrôle des systèmes de sécurité
• Lubrification et graissage
• Rapport détaillé d'intervention

Notre équipe intervient sur tous types d'équipements: tuyauteries, cuves, bacs de stockage, structures métalliques, etc.""",
                    'order': 1
                },
                {
                    'name': 'Maintenance corrective',
                    'description': """Service de maintenance corrective disponible 24h/24 pour réparer rapidement vos équipements en panne.

Nos services:
• Diagnostic rapide des pannes
• Réparation sur site ou en atelier
• Remplacement de pièces défectueuses
• Tests et mise en service
• Intervention d'urgence disponible

Nous intervenons dans les secteurs pétrolier, gazier, agroalimentaire et industriel.""",
                    'order': 2
                }
            ],
            'Constructions neuves et revamping': [
                {
                    'name': 'Construction neuve',
                    'description': """SICMI réalise la construction de nouvelles installations industrielles clé en main.

Nos réalisations:
• Charpentes métalliques
• Structures industrielles
• Plateformes et passerelles
• Bâtiments industriels
• Hangars et entrepôts

De la conception à la livraison, nous vous accompagnons à chaque étape du projet.""",
                    'order': 1
                },
                {
                    'name': 'Revamping et modernisation',
                    'description': """Modernisation et mise à niveau de vos installations existantes pour améliorer leurs performances.

Nos interventions:
• Réhabilitation d'équipements vieillissants
• Mise aux normes de sécurité
• Amélioration des performances
• Extension de capacité
• Optimisation énergétique

Nous prolongeons la vie de vos équipements tout en améliorant leur efficacité.""",
                    'order': 2
                }
            ],
            'Montage des bacs et cuves': [
                {
                    'name': 'Montage de bacs de stockage',
                    'description': """Expertise reconnue dans le montage de bacs de stockage pour l'industrie pétrolière et gazière.

Types de bacs:
• Bacs à toit fixe
• Bacs à toit flottant
• Bacs sous pression
• Réservoirs de différentes capacités

Nos certifications garantissent des réalisations conformes aux normes API et aux exigences de sécurité les plus strictes.""",
                    'order': 1
                },
                {
                    'name': 'Fabrication et montage de cuves',
                    'description': """Fabrication et installation de cuves industrielles sur mesure pour tous secteurs d'activité.

Applications:
• Cuves de stockage de produits chimiques
• Cuves agroalimentaires
• Cuves de process
• Cuves sous pression

Notre atelier de production nous permet de fabriquer des cuves aux dimensions exactes de vos besoins.""",
                    'order': 2
                }
            ],
            'Pose des tuyauteries et équipement  sur site': [
                {
                    'name': 'Tuyauterie industrielle',
                    'description': """Installation complète de réseaux de tuyauterie industrielle pour le transport de fluides.

Nos compétences:
• Tuyauterie haute pression
• Tuyauterie inox et acier carbone
• Réseaux de vapeur
• Réseaux de gaz
• Préfabrication en atelier

Nos soudeurs sont certifiés selon les normes internationales (ASME, EN, API).""",
                    'order': 1
                },
                {
                    'name': 'Montage d\'équipements sur site',
                    'description': """Installation et montage d'équipements industriels directement sur votre site.

Équipements installés:
• Échangeurs thermiques
• Colonnes et réacteurs
• Pompes et compresseurs
• Vannes et instruments
• Équipements de sécurité

Notre équipe mobile intervient partout au Cameroun et dans la sous-région.""",
                    'order': 2
                }
            ],
            'Pose d\'une passerelle, structures métalliques et équipements': [
                {
                    'name': 'Passerelles et escaliers métalliques',
                    'description': """Conception et installation de passerelles, escaliers et plateformes d'accès sécurisées.

Réalisations:
• Passerelles de circulation
• Escaliers industriels
• Plateformes d'accès
• Garde-corps et rampes
• Échelles à crinoline

Toutes nos réalisations respectent les normes de sécurité en vigueur.""",
                    'order': 1
                },
                {
                    'name': 'Structures métalliques',
                    'description': """Fabrication et montage de structures métalliques pour l'industrie et le bâtiment.

Types de structures:
• Charpentes métalliques
• Ossatures de bâtiments
• Supports d'équipements
• Structures offshore
• Portiques et potences

De la conception à l'installation, nous maîtrisons toute la chaîne de production.""",
                    'order': 2
                }
            ],
            'Travaux de Façade': [
                {
                    'name': 'Bardage et habillage métallique',
                    'description': """Pose de bardage et habillage métallique pour bâtiments industriels et commerciaux.

Nos prestations:
• Bardage simple et double peau
• Habillage en aluminium
• Couverture métallique
• Isolation thermique
• Étanchéité

Solutions esthétiques et durables pour protéger vos bâtiments.""",
                    'order': 1
                },
                {
                    'name': 'Menuiserie aluminium',
                    'description': """Fabrication et pose de menuiseries aluminium pour façades et bâtiments.

Produits:
• Fenêtres et baies vitrées
• Portes et portails
• Murs-rideaux
• Verrières
• Brise-soleil

Nos réalisations allient esthétique, performance thermique et durabilité.""",
                    'order': 2
                }
            ],
            'Travaux de rénovation': [
                {
                    'name': 'Rénovation industrielle',
                    'description': """Rénovation complète de vos installations industrielles pour les remettre à neuf.

Travaux réalisés:
• Réparation de structures métalliques
• Remplacement de tuyauteries
• Réfection de revêtements
• Mise en conformité
• Amélioration de l'isolation

Nous redonnons vie à vos installations vieillissantes.""",
                    'order': 1
                },
                {
                    'name': 'Traitement de surface et peinture',
                    'description': """Protection anticorrosion et peinture industrielle pour prolonger la durée de vie de vos équipements.

Nos services:
• Sablage et décapage
• Application de revêtements anticorrosion
• Peinture industrielle
• Revêtements époxy et polyuréthane
• Contrôle d'épaisseur et d'adhérence

Nous utilisons des produits certifiés et appliquons les normes ISO 12944.""",
                    'order': 2
                }
            ],
            'Accompagnement': [
                {
                    'name': 'Études et ingénierie',
                    'description': """Services d'études et d'ingénierie pour vos projets industriels.

Nos services:
• Études de faisabilité
• Conception et dimensionnement
• Plans d'exécution
• Calculs de structures
• Assistance technique

Notre bureau d'études vous accompagne de la conception à la réalisation.""",
                    'order': 1
                },
                {
                    'name': 'Conseil et expertise',
                    'description': """Conseil et expertise technique pour optimiser vos installations et projets.

Domaines d'expertise:
• Audit technique d'installations
• Expertise en corrosion
• Conseil en maintenance
• Optimisation de process
• Formation du personnel

Bénéficiez de notre expérience pour améliorer vos performances.""",
                    'order': 2
                }
            ]
        }

        services_created = 0
        services_updated = 0

        for category_name, services in services_data.items():
            # Trouver ou créer la catégorie
            category, cat_created = ServiceCategory.objects.get_or_create(
                name=category_name
            )
            if cat_created:
                self.stdout.write(f'  📂 Catégorie créée: {category_name}')

            for service_data in services:
                service, created = Service.objects.get_or_create(
                    name=service_data['name'],
                    category=category,
                    defaults={
                        'description': service_data['description'],
                        'order': service_data['order']
                    }
                )

                if created:
                    services_created += 1
                    self.stdout.write(
                        self.style.SUCCESS(f'    ✓ Service créé: {service.name}')
                    )
                else:
                    # Mettre à jour la description si elle existe déjà
                    service.description = service_data['description']
                    service.order = service_data['order']
                    service.save()
                    services_updated += 1
                    self.stdout.write(f'    ↺ Service mis à jour: {service.name}')

        self.stdout.write('\n' + '=' * 50)
        self.stdout.write(
            self.style.SUCCESS(f'✅ {services_created} services créés, {services_updated} mis à jour')
        )
