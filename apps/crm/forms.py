from django import forms
from .models import Lead, Client


class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['name', 'email', 'phone', 'status']
        widgets = {
            'name':   forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'email':  forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'phone':  forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'company']
        widgets = {
            'name':    forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'email':   forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'company': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company Name'}),
        }
