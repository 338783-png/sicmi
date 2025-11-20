from django.db import migrations

def clear_all_data(apps, schema_editor):
    """Supprimer toutes les données pour éviter les erreurs d'images"""
    Service = apps.get_model('sicmi_app', 'Service')
    ServiceImage = apps.get_model('sicmi_app', 'ServiceImage')
    Project = apps.get_model('sicmi_app', 'Project')
    ProjectImage = apps.get_model('sicmi_app', 'ProjectImage')
    Atelier = apps.get_model('sicmi_app', 'Atelier')
    AtelierImage = apps.get_model('sicmi_app', 'AtelierImage')
    TeamMember = apps.get_model('sicmi_app', 'TeamMember')
    
    # Supprimer toutes les données
    ServiceImage.objects.all().delete()
    ProjectImage.objects.all().delete()
    AtelierImage.objects.all().delete()
    Service.objects.all().delete()
    Project.objects.all().delete()
    Atelier.objects.all().delete()
    TeamMember.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('sicmi_app', '0013_fix_atelier_image_path_length'),
    ]

    operations = [
        migrations.RunPython(clear_all_data, migrations.RunPython.noop),
    ]
