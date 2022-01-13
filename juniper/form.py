from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import JuniperCase

class JuniperCaseForm(forms.ModelForm):

    class Meta:
        model = JuniperCase
        fields = ("id", "author", "created_date", "case_num", "title", "serial", "part", "symptom", "solution")