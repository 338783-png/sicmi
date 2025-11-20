from django.db import migrations


def clear_all_data(apps, schema_editor):
    """Supprimer toutes les données pour éviter les erreurs d'image"""
    ServiceImage = apps.get_model('sicmi_app', 'ServiceImage')
    ProjectImage = apps.get_model('sicmi_app', 'ProjectImage')
    AtelierImage = apps.get_model('sicmi_app', 'AtelierImage')
    Service = apps.get_model('sicmi_app', 'Service')
    Project = apps.get_model('sicmi_app', 'Project')
    Atelier = apps.get_model('sicmi_app', 'Atelier')
    TeamMember = apps.get_model('sicmi_app', 'TeamMember')
    
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
