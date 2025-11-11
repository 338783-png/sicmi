from django import forms
from .models import ContactRequest

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactRequest
        fields = ['name', 'company', 'email', 'phone', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Votre nom complet'}),
            'company': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Votre entreprise (optionnel)'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Votre adresse email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Votre numéro de téléphone'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sujet de votre message'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Votre message', 'rows': 5}),
        }