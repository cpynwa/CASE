from django import forms
from django.utils.translation import gettext_lazy as _
from .models import ExtremeCase

class ExtremeCaseForm(forms.ModelForm):

    class Meta:
        model = ExtremeCase
        fields = ["title", "symptom", "conclusion", "site", "vendor_case_num", "os_ver", "serial", "part", "hostname", "progress"]
        labels = {
            'install_date': _('설치일'),
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'symptom': forms.Textarea(attrs={'class': 'form-control'}),
            'conclusion': forms.Textarea(attrs={'class': 'form-control'}),
            'site': forms.TextInput(attrs={'class': 'form-control'}),
            'vendor_case_num': forms.TextInput(attrs={'class': 'form-control'}),
            'os_ver': forms.TextInput(attrs={'class': 'form-control'}),
            'serial': forms.TextInput(attrs={'class': 'form-control'}),
            'part': forms.TextInput(attrs={'class': 'form-control'}),
            'hostname': forms.TextInput(attrs={'class': 'form-control'}),
            'progress': forms.Select(attrs={'class': 'form-control'}),
        }
