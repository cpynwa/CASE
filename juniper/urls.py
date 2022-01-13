from django.urls import path
from . import views

urlpatterns = [
    path('juniper/main', views.JuniperCaseMain, name='JuniperCaseMain'),
]