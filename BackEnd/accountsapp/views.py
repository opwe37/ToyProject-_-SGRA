import os

from django.shortcuts import render, redirect

# Create your views here.


def index(request):
    return render(request, 'base.html')

def login(request):
    return render(request, 'accountsapp/auth.html')

def kakao_login(request):
    app_rest_api_key = os.environ.get("KAKAO_REST_API_KEY")
    redirect_uri = "http://127.0.0.1:8000/authaccounts/kakao/login/callback/"
    return redirect(
        f"https://kauth.kakao.com/oauth/authorize?client_id={'8e9317a3618e409d909c909556351392'}&redirect_uri={'http://127.0.0.1:8000/authaccounts/kakao/login/callback/'}&response_type=code"
    )