from django.urls import path, include 
from django.contrib.auth import views as auth_views
from connexion import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='connexion/login.html'), name = 'login'),
]