from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView

from commentapp.forms import CommentCreationForm
from commentapp.models import Comment


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreationForm
    success_url = '/'
    template_name = 'commentapp/create.html'

    def form_valid(self, form):
        form.instance.writer = self.request.user
        return super().form_valid(form)


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

