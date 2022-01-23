from django.urls import path
from . import views

urlpatterns = [
    path('extreme/list', views.data_list, name='extreme_list'),
    path('extreme/<int:pk>/', views.data_detail, name='extreme_detail'),
    path('extreme/new', views.data_new, name='extreme_new'),
    path('extreme/<int:pk>/edit/', views.data_edit, name='extreme_edit'),
    path('extreme/search', views.search, name='extreme_search'),
    path('extreme/detail/<int:pk>/delete', views.data_delete, name='extreme_delete'),
    path('extreme/list/export', views.data_export, name='extreme_export'),
]