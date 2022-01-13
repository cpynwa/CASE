from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import JuniperCase

# Register your models here.
# Register your models here.
@admin.register(JuniperCase)
class JuniperCaseAdmin(ImportExportModelAdmin):
    list_display = ["id", "author", "created_date", "case_num", "title", "serial", "part"]
    list_display_links = ["id", "case_num", "title"]
    search_fields = ["case_num", "title", "serial", "part", "symptom", "solution"]