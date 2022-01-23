from django.urls import path
from . import views

urlpatterns = [
    # path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('change_password', views.change_password, name='change_password'),
]