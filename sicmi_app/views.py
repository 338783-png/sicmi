from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Service, Project, TeamMember, ContactRequest
from .forms import ContactForm
from django.contrib.admin.views.decorators import staff_member_required





def home(request):
    services = Service.objects.all()[:6]
    recent_projects = Project.objects.all()[:3]
    context = {
        'services': services,
        'recent_projects': recent_projects,
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
        services_by_category[category[1]] = Service.objects.filter(category=category[0])
    
    context = {
        'services_by_category': services_by_category,
    }
    return render(request, 'services.html', context)

def service_detail(request, service_id):
    service = Service.objects.get(id=service_id)
    related_projects = Project.objects.filter(services=service)[:3]
    
    context = {
        'service': service,
        'related_projects': related_projects,
    }
    return render(request, 'services_detail.html', context)
def projects(request):
    try:
        projects_list = Project.objects.all()
        paginator = Paginator(projects_list, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    except:
        # Données temporaires pour tester
        projects_list = []
        page_obj = []
    
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'projects.html', context)

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


@staff_member_required
def manage_dashboard(request):
    """Frontend admin dashboard: show quick stats and recent contact requests."""
    services_count = Service.objects.count()
    projects_count = Project.objects.count()
    team_count = TeamMember.objects.count()
    contacts_count = ContactRequest.objects.count()

    recent_contacts = ContactRequest.objects.all()[:8]

    context = {
        'services_count': services_count,
        'projects_count': projects_count,
        'team_count': team_count,
        'contacts_count': contacts_count,
        'recent_contacts': recent_contacts,
    }
    return render(request, 'admin/dashboard.html', context)