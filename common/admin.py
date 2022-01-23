from django.contrib import admin
from django.contrib.admin.models import LogEntry
from import_export.admin import ImportExportModelAdmin
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from extreme.models import ExtremeCase
from juniper.models import JuniperCase

# Register your models here.
@admin.register(ExtremeCase)
class ExtremeCaseAdmin(ImportExportModelAdmin):
    list_display = ["id", "created_date", "case_num", "site", "title", "part", "manager", "progress"]
    list_display_links = ["id", "case_num", "title"]
    search_fields = ["manager", "site", "os_ver", "case_num", "title", "serial", "part", "symptom", "conclusion",
                     "progress"]


@admin.register(JuniperCase)
class JuniperCaseAdmin(ImportExportModelAdmin):
    list_display = ["id", "created_date", "case_num", "site", "title", "part", "manager", "progress"]
    list_display_links = ["id", "case_num", "title"]
    search_fields = ["manager", "site", "os_ver", "case_num", "title", "serial", "part", "symptom", "conclusion", "progress"]


class LogEntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_user', 'get_string', 'action_time', 'object_id')
    actions = None

    def get_string(self, obj):
        return str(obj)

    get_string.short_description = 'action'

    def get_user(self, obj):
        return str(obj.user.username)
    get_user.short_description = 'User'

    search_fields = ['=user__username', ]
    fieldsets = [
        (None, {'fields':()}),
        ]

    def __init__(self, *args, **kwargs):
        super(LogEntryAdmin, self).__init__(*args, **kwargs)
        self.list_display_links = None


admin.site.register(admin.models.LogEntry, LogEntryAdmin)