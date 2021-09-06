import json

import self
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DeleteView, RedirectView

from articleapp.models import Article
from commentapp.forms import CommentCreationForm
from commentapp.models import Comment


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreationForm
    success_url = reverse_lazy('commentapp:list')
    template_name = 'commentapp/create.html'

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        parent = Comment.objects.get(pk=data['parent_pk']) if 'parent_pk' in data else None
        Comment(writer=request.user, content=data['content'],
                parent=parent, secret=data['secret'],
                article_id=data['article_pk']).save()

        return self.get_success_url();


    def get_success_url(self):
        return HttpResponse(reverse('commentapp:list'))


class CommentUpdateView(RedirectView):

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        target_comment = Comment.objects.get(pk=kwargs['pk'])
        target_comment.content = data['content']
        target_comment.secret = data['secret']
        target_comment.save()
        return super().post(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        return reverse('commentapp:list')


class CommentListView(ListView):
    model = Comment
    context_object_name = 'comment_list'
    template_name = 'commentapp/list.html'
    paginate_by = 10


class CommentDeleteView(DeleteView):
    model = Comment
    success_url = reverse_lazy('commentapp:list')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

