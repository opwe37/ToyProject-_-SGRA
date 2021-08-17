import allauth.account.views
from django.urls import path, include

import accountsapp.views
from accountsapp import views

app_name = 'accountsapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', accountsapp.views.login, name='login'),
    path('logout/', allauth.account.views.LogoutView.as_view(), name='logout'),
]