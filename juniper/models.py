from django.db import models
from django.conf import settings
from datetime import datetime

# case_num date format setting
dt_now = datetime.now()
nowdate = dt_now.strftime('%Y-%m-%d-%H-%M') # 2022-01-11-04-30
# Create your models here.

class JuniperCase(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='case_data')
    created_date = models.DateTimeField(default=datetime.now())
    case_num = models.CharField(unique=True, max_length=16, default=nowdate)
    title = models.CharField(max_length=100)
    serial = models.CharField(max_length=25, null=True, blank=True)
    part = models.CharField(max_length=100)
    symptom = models.TextField()
    soultion = models.TextField(null=True, blank=True)