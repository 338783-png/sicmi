from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('a-propos/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('services/<int:service_id>/', views.service_detail, name='service_detail'),
    path('projets/', views.projects, name='projects'),
    path('projets/<int:project_id>/', views.project_detail, name='project_detail'),
    path('realisations/', views.realisations, name='realisations'),
    path('realisations/<int:realisation_id>/', views.realisation_detail, name='realisation_detail'),
    path('contact/', views.contact, name='contact'),
    path('politique-qhse/', views.qhse_policy, name='qhse_policy'),
    path('engagement-rse/', views.rse_engagement, name='rse_engagement'),
]