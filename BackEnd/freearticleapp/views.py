from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, FormView
from django.views.generic.edit import FormMixin
from django.views.generic.list import MultipleObjectMixin

from commentapp.forms import CommentCreationForm
from freearticleapp.decorators import article_ownership_required
from freearticleapp.forms import ArticleCreationForm, PostSearchForm
from freearticleapp.models import FreeArticle


class ArticleListView(ListView):
    model = FreeArticle
    context_object_name = 'article_free_list'
    template_name = 'freearticleapp/free_list.html'
    paginate_by = 20


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ArticleCreateView(CreateView):
    model = FreeArticle
    form_class = ArticleCreationForm
    template_name = 'freearticleapp/create.html'

    def form_valid(self, form):
        form.instance.writer = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('freearticleapp:detail', kwargs={'pk': self.object.pk})


class ArticleDetailView(DetailView, FormMixin):
    model = FreeArticle
    context_object_name = 'target_article'
    form_class = CommentCreationForm
    template_name = 'freearticleapp/detail.html'

    def get(self, request, *args, **kwargs):

        clicked_article = FreeArticle.objects.get(pk=kwargs['pk'])
        clicked_article.hits += 1
        clicked_article.save()
        print(clicked_article.hits)
        return super().get(request, *args, **kwargs)


@method_decorator(article_ownership_required, 'get')
@method_decorator(article_ownership_required, 'post')
class ArticleUpdateView(UpdateView):
    model = FreeArticle
    form_class = ArticleCreationForm
    context_object_name = 'target_article'
    template_name = 'freearticleapp/update.html'

    def get_success_url(self):
        return reverse('freearticleapp:detail', kwargs={'pk': self.object.pk})


@method_decorator(article_ownership_required, 'get')
@method_decorator(article_ownership_required, 'post')
class ArticleDeleteView(DeleteView):
    model = FreeArticle
    context_object_name = 'target_article'
    success_url = reverse_lazy('freearticleapp:list')
    template_name = 'freearticleapp/delete.html'


class SearchFormView(FormView):
    form_class = PostSearchForm
    template_name = 'freearticleapp/post_search.html'

    def form_valid(self, form):
        searchWord = form.cleaned_data['search_word']
        post_list = FreeArticle.objects.filter(Q(title__icontains=searchWord) | Q(content__icontains=searchWord) | Q(writer__username__icontains=searchWord)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = post_list

        return render(self.request, self.template_name, context)

class FreeArticleHomeView(ListView):
    model = FreeArticle
    context_object_name = 'article_free_list'
    template_name = 'freearticleapp/home.html'

    def get_queryset(self):
        return FreeArticle.objects.order_by('-created_at')[:5]