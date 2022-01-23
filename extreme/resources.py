from import_export import resources
from django.utils.translation import gettext_lazy as _
from .models import ExtremeCase

class ExtremeCaseResource(resources.ModelResource):
    class Meta:
        model = ExtremeCase
        fields = ("title", "symptom", "conclusion", "site", "os_ver", "serial", "part", "progress")