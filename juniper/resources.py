from import_export import resources
from django.utils.translation import gettext_lazy as _
from .models import JuniperCase

class JuniperCaseResource(resources.ModelResource):
    class Meta:
        model = JuniperCase
        fields = ("title", "symptom", "conclusion", "site", "os_ver", "serial", "part", "progress")
