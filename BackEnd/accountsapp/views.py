from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'base.html')

def login(request):
    return render(request, 'accountsapp/auth.html')

