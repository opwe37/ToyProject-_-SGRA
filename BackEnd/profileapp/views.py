from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import DetailView

# Create your views here.

# profile create는... 회원가입할 때, 자동으로 만들어져서
# 기본 세팅이 되어 있어야하는거 아니야?

# All-Auth의 Adapter를 활용해야 할지도...
from profileapp.models import Profile


class ProfileDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'profileapp/detail.html'