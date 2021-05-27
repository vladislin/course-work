from django import forms
from .models import *


class AddSchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = '__all__'
        widgets = {
            'sc_name': forms.TextInput(attrs={'class': 'form-control'}),
            'sc_manager': forms.TextInput(attrs={'class': 'form-control'}),
            'sc_address': forms.TextInput(attrs={'class': 'form-control'}),
            'sc_site': forms.TextInput(attrs={'class': 'form-control'}),
            'sc_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'sc_lat': forms.TextInput(attrs={'class': 'form-control'}),
            'sc_lon': forms.TextInput(attrs={'class': 'form-control'}),
        }


class AddUniversityForm(forms.ModelForm):
    class Meta:
        model = University
        fields = '__all__'
        widgets = {
            'un_name': forms.TextInput(attrs={'class': 'form-control'}),
            'un_manager': forms.TextInput(attrs={'class': 'form-control'}),
            'un_address': forms.TextInput(attrs={'class': 'form-control'}),
            'un_site': forms.TextInput(attrs={'class': 'form-control'}),
            'un_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'un_lat': forms.TextInput(attrs={'class': 'form-control'}),
            'un_lon': forms.TextInput(attrs={'class': 'form-control'}),
        }
