import os

from django.shortcuts import render, redirect

# Create your views here.


def index(request):
    return render(request, 'base.html')

def login(request):
    return render(request, 'accountsapp/auth.html')