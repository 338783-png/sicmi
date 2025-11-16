from django.contrib import admin
from .models import Service, ServiceImage, Project, ProjectImage, TeamMember, ContactRequest, QHSEPolicy
from .models import RealisationCategory, Realisation, RealisationImage


class RealisationImageInline(admin.TabularInline):
    model = RealisationImage
    extra = 1

@admin.register(RealisationCategory)
class RealisationCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'order']
    search_fields = ['name', 'description']

@admin.register(Realisation)
class RealisationAdmin(admin.ModelAdmin):
    list_display = ['title', 'client', 'category', 'completion_date']
    list_filter = ['category', 'completion_date']
    search_fields = ['title', 'client', 'description', 'location']
    inlines = [RealisationImageInline]

class ServiceImageInline(admin.TabularInline):
    model = ServiceImage
    extra = 1

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'order']
    list_filter = ['category']
    search_fields = ['name', 'description']
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

@admin.register(QHSEPolicy)
class QHSEPolicyAdmin(admin.ModelAdmin):
    list_display = ['title', 'version', 'effective_date', 'is_active']
    list_filter = ['is_active', 'effective_date']
    search_fields = ['title', 'content']