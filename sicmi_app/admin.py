from django.contrib import admin
from .models import Service, ServiceCategory, ServiceImage, Project, ProjectImage, TeamMember, ContactRequest, Atelier, AtelierImage

@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

class ServiceImageInline(admin.TabularInline):
    model = ServiceImage
    extra = 1

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'order']
    list_filter = ['category']
    search_fields = ['name', 'description']
    list_editable = ['order']
    inlines = [ServiceImageInline]

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'client', 'completion_date']
    list_filter = ['completion_date']
    search_fields = ['title', 'client', 'description']
    inlines = [ProjectImageInline]

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'order']
    search_fields = ['name', 'position', 'specialization']

@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at', 'is_processed']
    list_filter = ['is_processed', 'created_at']
    search_fields = ['name', 'email', 'subject', 'message']


class AtelierImageInline(admin.TabularInline):
    model = AtelierImage
    extra = 1


@admin.register(Atelier)
class AtelierAdmin(admin.ModelAdmin):
    list_display = ['name', 'order']
    list_editable = ['order']
    search_fields = ['name', 'description']
    inlines = [AtelierImageInline]

