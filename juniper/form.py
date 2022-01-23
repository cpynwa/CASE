from django import forms
from django.utils.translation import gettext_lazy as _
from .models import JuniperCase

class JuniperCaseForm(forms.ModelForm):

    class Meta:
        model = JuniperCase
        fields = ["title", "symptom", "conclusion", "site", "os_ver", "serial", "part", "progress"]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'symptom': forms.Textarea(attrs={'class': 'form-control'}),
            'conclusion': forms.Textarea(attrs={'class': 'form-control'}),
            'site': forms.TextInput(attrs={'class': 'form-control'}),
            'os_ver': forms.TextInput(attrs={'class': 'form-control'}),
            'serial': forms.TextInput(attrs={'class': 'form-control'}),
            'part': forms.TextInput(attrs={'class': 'form-control'}),
            'progress': forms.Select(attrs={'class': 'form-control'}),
        }