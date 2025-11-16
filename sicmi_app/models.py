from django.db import models

class Service(models.Model):
    CATEGORY_CHOICES = [
        ('construction', 'Constructions neuves et revamping'),
        ('maintenance', 'Maintenance industrielle'),
        ('accompagnement', 'Accompagnement'),
        ('facade', 'Travaux de Façade'),
        ('renovation', 'Travaux de rénovation'),
    ]
    
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField()
    main_image = models.ImageField(upload_to='services/', blank=True, null=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order', 'name']
    
    def __str__(self):
        return self.name

class ServiceImage(models.Model):
    service = models.ForeignKey(Service, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='services/gallery/')
    caption = models.CharField(max_length=200, blank=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']

class Project(models.Model):
    title = models.CharField(max_length=200)
    client = models.CharField(max_length=200)
    description = models.TextField()
    main_image = models.ImageField(upload_to='projects/')
    completion_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-completion_date']
    
    def __str__(self):
        return f"{self.title} - {self.client}"

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='projects/gallery/')
    caption = models.CharField(max_length=200, blank=True)
    is_primary = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    specialization = models.CharField(max_length=200)
    image = models.ImageField(upload_to='team/', blank=True, null=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order', 'name']
    
    def __str__(self):
        return f"{self.name} - {self.position}"

class ContactRequest(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_processed = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.subject}"

class QHSEPolicy(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    version = models.CharField(max_length=20, default='1.0')
    effective_date = models.DateField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-effective_date']
        verbose_name_plural = 'QHSE Policies'
    
    def __str__(self):
        return f"{self.title} - v{self.version}"
    
class RealisationCategory(models.Model):
    name = models.CharField(max_length=100)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order', 'name']
        verbose_name_plural = 'Realisation Categories'
    
    def __str__(self):
        return self.name

class Realisation(models.Model):
    title = models.CharField(max_length=200)
    client = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(RealisationCategory, on_delete=models.CASCADE, related_name='realisations')
    main_image = models.ImageField(upload_to='realisations/')
    completion_date = models.DateField()
    location = models.CharField(max_length=200, blank=True)
    duration = models.CharField(max_length=100, blank=True, help_text="Ex: 3 mois, 6 semaines")
    budget = models.CharField(max_length=100, blank=True, help_text="Ex: 50M FCFA")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-completion_date']
    
    def __str__(self):
        return f"{self.title} - {self.client}"

class RealisationImage(models.Model):
    realisation = models.ForeignKey(Realisation, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='realisations/gallery/')
    caption = models.CharField(max_length=200, blank=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']