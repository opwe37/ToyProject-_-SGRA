from django.contrib.auth.views import LoginView
from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [
    path('login/', LoginView.as_view(template_name='accountsapp/login.html'), name='login'),
]