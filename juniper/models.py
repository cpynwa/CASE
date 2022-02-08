from django.db import models
from django.conf import settings
from django.utils import timezone

# case_num date format setting
case_id = timezone.now().strftime('%Y-%m%d-%H%M%S') # 2022-01-11-043020
# Create your models here.

class JuniperCase(models.Model):
    manager = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='juniper_case')
    created_date = models.DateTimeField(default=timezone.now)
    case_num = models.CharField(unique=True, max_length=19, default=case_id)
    vendor_case_num = models.CharField(unique=True, null=True, blank=True, max_length=20)
    site = models.CharField(max_length=20, null=True, blank=True)
    part = models.CharField(max_length=50, null=True, blank=True)
    serial = models.CharField(max_length=25, null=True, blank=True)
    os_ver = models.CharField(max_length=25, null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    symptom = models.TextField()
    conclusion = models.TextField(null=True, blank=True)
    progress_choices = (('진행중', '진행중'), ('진행완료', '진행완료'), ('보류', '보류'))
    progress = models.CharField(max_length=10, choices=progress_choices)
    hostname = models.CharField(max_length=25, null=True, blank=True)
