from django.urls import path
from . import views
from .views_debug import cloudinary_debug

urlpatterns = [
    path('', views.home, name='home'),
    path('a-propos/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('services/<int:service_id>/', views.service_detail, name='service_detail'),
    path('projets/', views.projects, name='projects'),
    path('projets/<int:project_id>/', views.project_detail, name='project_detail'),
    path('contact/', views.contact, name='contact'),
    path('politique-qhse/', views.qhse_policy, name='qhse_policy'),
    path('ateliers/', views.ateliers, name='ateliers'),
    path('ateliers/<slug:atelier_id>/', views.atelier_detail, name='atelier_detail'),
    path('recherche/', views.search, name='search'),
    path('equipe/', views.team, name='team'),
    path('debug/cloudinary/', cloudinary_debug, name='cloudinary_debug'),
]