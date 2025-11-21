from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.core.mail import send_mail
from django.conf import settings
from .models import Service, ServiceCategory, Project, TeamMember, ServiceImage, ProjectImage, Atelier, AtelierImage
from .forms import ContactForm

def home(request):
    services = Service.objects.select_related('category').all()[:6]
    recent_projects = Project.objects.prefetch_related('images').all()[:3]
    ateliers = Atelier.objects.prefetch_related('images').all()[:4]
    
    # Récupérer les images de fond pour l'héros
    hero_images = ProjectImage.objects.filter(is_primary=True).select_related('project')[:5]
    
    context = {
        'services': services,
        'recent_projects': recent_projects,
        'hero_images': hero_images,
        'ateliers': ateliers,
    }
    return render(request, 'index.html', context)

def about(request):
    team_members = TeamMember.objects.all()
    context = {
        'team_members': team_members,
    }
    return render(request, 'about.html', context)

def services(request):
    # Raggruppa servizi per categoria
    services_by_category = {}
    categories = ServiceCategory.objects.all().prefetch_related('services')
    
    for category in categories:
        services_list = category.services.all()
        if services_list.exists():
            services_by_category[category.name] = services_list

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
        
        # Filtre par service
        service_filter = request.GET.get('service')
        if service_filter:
            # Mapper les slugs aux catégories de services
            service_mapping = {
                'construction': 'Constructions neuves',
                'maintenance': 'Maintenance industrielle',
                'accompagnement': 'Accompagnement',
                'facade': 'Travaux de façade',
                'renovation': 'Rénovation'
            }
            
            if service_filter in service_mapping:
                service_name = service_mapping[service_filter]
                # Filtrer les projets dont le service contient ce nom
                projects_list = projects_list.filter(service__icontains=service_name)
        
        paginator = Paginator(projects_list, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    except Exception as e:
        print(f"Erreur: {e}")
        page_obj = []

    context = {
        'page_obj': page_obj,
        'current_filter': service_filter if service_filter else 'all',
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
            contact_request = form.save()
            
            # NOTE: Envoi d'email désactivé temporairement car trop lent sur Render free tier
            # Les messages sont quand même sauvegardés dans la base de données
            # et accessibles via l'admin Django
            
            messages.success(request, 'Votre message a été enregistré avec succès. Nous vous contacterons bientôt.')
            
            # Rediriger vers la page de confirmation avec les détails
            return redirect('contact_confirmation', contact_id=contact_request.id)
    else:
        form = ContactForm()

    context = {
        'form': form,
    }
    return render(request, 'contact.html', context)

def contact_confirmation(request, contact_id):
    """Page de confirmation après envoi d'un message de contact"""
    contact_request = get_object_or_404(ContactRequest, id=contact_id)
    
    context = {
        'contact': contact_request,
    }
    return render(request, 'contact_confirmation.html', context)

def qhse_policy(request):
    """Page statique de la politique QHSE & RSE combinée"""
    context = {
        'page_title': 'Politique QHSE & RSE',
    }
    return render(request, 'qhse_policy.html', context)

def ateliers(request):
    """Page des ateliers et équipements avec images depuis la base de données"""
    ateliers_list = Atelier.objects.all().prefetch_related('images')
    
    context = {
        'ateliers': ateliers_list,
    }
    return render(request, 'ateliers.html', context)


def atelier_detail(request, atelier_id):
    """Affiche la page détaillée pour un atelier donné"""
    atelier = get_object_or_404(Atelier, id=atelier_id)
    atelier_images = atelier.images.all()
    
    # Autres ateliers pour la section similaire
    other_ateliers = Atelier.objects.exclude(id=atelier.id)[:3]
    
    context = {
        'atelier': atelier,
        'atelier_images': atelier_images,
        'other_ateliers': other_ateliers,
    }
    return render(request, 'atelier_detail.html', context)


def search(request):
    """Vista per la ricerca globale"""
    query = request.GET.get('q', '').strip()
    
    services_results = []
    projects_results = []
    
    if query:
        # Cerca nei servizi (inclusa la categoria)
        services_results = Service.objects.filter(
            Q(name__icontains=query) | 
            Q(description__icontains=query) |
            Q(category__name__icontains=query)
        ).distinct()[:10]
        
        # Cerca nei progetti
        projects_results = Project.objects.filter(
            Q(title__icontains=query) | 
            Q(description__icontains=query) |
            Q(client__icontains=query)
        ).distinct()[:10]
    
    context = {
        'query': query,
        'services_results': services_results,
        'projects_results': projects_results,
        'total_results': len(services_results) + len(projects_results),
    }
    return render(request, 'search.html', context)


def team(request):
    """Page de l'équipe"""
    team_members = TeamMember.objects.all()
    
    context = {
        'team_members': team_members,
    }
    return render(request, 'team.html', context)