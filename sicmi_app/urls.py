from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('a-propos/', views.about, name='about'),
    path('manage/', views.manage_dashboard, name='manage_dashboard'),
    path('manage/settings/', views.manage_site_settings, name='manage_site_settings'),
    path('services/', views.services, name='services'),
    path('services/<int:service_id>/', views.service_detail, name='service_detail'),
    path('projets/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
]