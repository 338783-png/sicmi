from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Service, Project, TeamMember, QHSEPolicy, ServiceImage, ProjectImage
from .forms import ContactForm
from .models import Realisation, RealisationCategory, RealisationImage

def realisations(request):
    """Page principale des réalisations"""
    categories = RealisationCategory.objects.all()
    realisations_list = Realisation.objects.all().select_related('category').prefetch_related('images')
    
    # Pagination
    paginator = Paginator(realisations_list, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'categories': categories,
        'page_obj': page_obj,
    }
    return render(request, 'realisations.html', context)

def realisation_detail(request, realisation_id):
    """Détail d'une réalisation"""
    realisation = get_object_or_404(Realisation, id=realisation_id)
    realisation_images = realisation.images.all()
    
    # Réalisations similaires (même catégorie)
    similar_realisations = Realisation.objects.filter(
        category=realisation.category
    ).exclude(id=realisation.id)[:3]
    
    context = {
        'realisation': realisation,
        'realisation_images': realisation_images,
        'similar_realisations': similar_realisations,
    }
    return render(request, 'realisation_detail.html', context)

def home(request):
    services = Service.objects.all()[:6]
    recent_projects = Project.objects.all()[:3]
    qhse_policy = QHSEPolicy.objects.filter(is_active=True).first()
    
    # Récupérer les images de fond pour l'héros
    hero_images = ProjectImage.objects.filter(is_primary=True)[:5]
    
    context = {
        'services': services,
        'recent_projects': recent_projects,
        'qhse_policy': qhse_policy,
        'hero_images': hero_images,
    }
    return render(request, 'index.html', context)

def about(request):
    team_members = TeamMember.objects.all()
    context = {
        'team_members': team_members,
    }
    return render(request, 'about.html', context)

def services(request):
    services_by_category = {}
    for category in Service.CATEGORY_CHOICES:
        services = Service.objects.filter(category=category[0])
        services_by_category[category[1]] = services

    context = {
        'services_by_category': services_by_category,
    }
    return render(request, 'services.html', context)

def service_detail(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    service_images = service.images.all()

    context = {
        'service': service,
        'service_images': service_images,
    }
    return render(request, 'services_detail.html', context)

def projects(request):
    try:
        projects_list = Project.objects.all().prefetch_related('images')
        paginator = Paginator(projects_list, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    except Exception as e:
        print(f"Erreur: {e}")
        page_obj = []

    context = {
        'page_obj': page_obj,
    }
    return render(request, 'projects.html', context)

def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    project_images = project.images.all()
    
    # Autres projets pour la section similaire
    other_projects = Project.objects.exclude(id=project.id)[:3]
    
    context = {
        'project': project,
        'project_images': project_images,
        'other_projects': other_projects,
    }
    return render(request, 'project_detail.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Votre message a été envoyé avec succès. Nous vous contacterons bientôt.')
            return redirect('contact')
    else:
        form = ContactForm()

    context = {
        'form': form,
    }
    return render(request, 'contact.html', context)

def qhse_policy(request):
    qhse_policies = QHSEPolicy.objects.filter(is_active=True)
    context = {
        'qhse_policies': qhse_policies,
    }
    return render(request, 'qhse_policy.html', context)

def rse_engagement(request):
    context = {
        'page_title': 'Engagement RSE',
    }
    return render(request, 'rse_engagement.html', context)

def ateliers(request):
    """Page descriptive des ateliers et équipements"""
    # Informations statiques pour la page; on peut plus tard les tirer d'un modèle si besoin
    ateliers_info = [
        {
            'id': 'production',
            'title': "Atelier de production",
            'summary': "Grande surface dédiée à la fabrication et à l'assemblage de structures métalliques.",
            'details': "Nos ateliers de production sont équipés pour la découpe, le pliage, le soudage et l'assemblage de grandes structures. Nous respectons des procédures QHSE strictes et gérons les flux logistiques pour des livraisons fiables."
        },
        {
            'id': 'usinage',
            'title': "Atelier d'usinage",
            'summary': "Postes d'usinage CNC et traditionnels pour pièces de précision.",
            'details': "Postes CNC modernes et outillage de contrôle assurent des tolérances serrées pour pièces mécaniques et ensembles. Notre équipe réalise usinage, rectification et finition selon les plans techniques."
        },
        {
            'id': 'assemblage',
            'title': "Atelier d'assemblage",
            'summary': "Zones d'assemblage équipées pour montage, tests et mise en service.",
            'details': "Zones dédiées pour le montage mécanique et électrique, bancs de test fonctionnels et équipes d'essais pour s'assurer de la conformité et de la performance avant livraison."
        },
        {
            'id': 'equipements',
            'title': "Équipements & Machines",
            'summary': "CNC, presses hydrauliques, soudeuses, systèmes de levage et outillage spécialisé.",
            'details': "Nous investissons continuellement dans des équipements pour augmenter la capacité et la qualité : CNC 3-axes/5-axes, lignes de soudure semi-automatiques, presses, palans et contrôles non destructifs."
        },
    ]

    context = {
        'ateliers_info': ateliers_info,
    }
    return render(request, 'ateliers.html', context)


def atelier_detail(request, atelier_id):
    """Affiche la page détaillée pour un atelier donné (atelier_id = production|usinage|assemblage|equipements)"""
    ateliers_info = [
        {
            'id': 'production',
            'title': "Atelier de production",
            'summary': "Grande surface dédiée à la fabrication et à l'assemblage de structures métalliques.",
            'details': "Nos ateliers de production sont équipés pour la découpe, le pliage, le soudage et l'assemblage de grandes structures. Nous respectons des procédures QHSE strictes et gérons les flux logistiques pour des livraisons fiables."
        },
        {
            'id': 'usinage',
            'title': "Atelier d'usinage",
            'summary': "Postes d'usinage CNC et traditionnels pour pièces de précision.",
            'details': "Postes CNC modernes et outillage de contrôle assurent des tolérances serrées pour pièces mécaniques et ensembles. Notre équipe réalise usinage, rectification et finition selon les plans techniques."
        },
        {
            'id': 'assemblage',
            'title': "Atelier d'assemblage",
            'summary': "Zones d'assemblage équipées pour montage, tests et mise en service.",
            'details': "Zones dédiées pour le montage mécanique et électrique, bancs de test fonctionnels et équipes d'essais pour s'assurer de la conformité et de la performance avant livraison."
        },
        {
            'id': 'equipements',
            'title': "Équipements & Machines",
            'summary': "CNC, presses hydrauliques, soudeuses, systèmes de levage et outillage spécialisé.",
            'details': "Nous investissons continuellement dans des équipements pour augmenter la capacité et la qualité : CNC 3-axes/5-axes, lignes de soudure semi-automatiques, presses, palans et contrôles non destructifs."
        },
    ]

    atelier = next((a for a in ateliers_info if a['id'] == atelier_id), None)
    if not atelier:
        # return to ateliers listing if unknown
        return redirect('ateliers')

    context = {
        'atelier': atelier,
    }
    return render(request, 'atelier_detail.html', context)