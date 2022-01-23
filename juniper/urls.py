from django.urls import path
from . import views

urlpatterns = [
    path('juniper/list', views.data_list, name='juniper_list'),
    path('juniper/<int:pk>/', views.data_detail, name='juniper_detail'),
    path('juniper/new', views.data_new, name='juniper_new'),
    path('juniper/<int:pk>/edit/', views.data_edit, name='juniper_edit'),
    path('juniper/search', views.search, name='juniper_search'),
    path('juniper/detail/<int:pk>/delete', views.data_delete, name='juniper_delete'),
    path('juniper/list/export', views.data_export, name='juniper_export'),
]