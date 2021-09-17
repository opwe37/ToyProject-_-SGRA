import json

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views import View
from django.views.generic import DetailView
from django.views.generic.list import MultipleObjectMixin

from articleapp.models import Article
from commentapp.models import Comment
from freearticleapp.models import FreeArticle
from profileapp.models import Profile


class ProfileDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'profileapp/detail.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        selected_tab = self.request.GET.get('tab')
        if selected_tab == 'study':
            context['object_list'] = Article.objects.filter(writer_id=kwargs['object'].pk)
        elif selected_tab == 'free':
            context['object_list'] = FreeArticle.objects.filter(writer_id=kwargs['object'].pk)
        else:
            context['object_list'] = Comment.objects.filter(writer_id=kwargs['object'].pk)

        return context


class ProfileUpdateRView(View):

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        target = Profile.objects.get(user_id=kwargs['pk'])

        target.message = data['message']
        target.save()

        response = HttpResponse()
        response.status_code = 200
        response.reason_phrase = 'OK'

        return response
