from django.contrib.auth.decorators import login_required

# Create your views here.
from django.db.models import Q
from django.shortcuts import render

from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView, FormView
from django.views.generic.edit import FormMixin

from articleapp.decorators import article_ownership_required
from articleapp.forms import ArticleCreationForm, PostSearchForm
from articleapp.models import Article
from commentapp.forms import CommentCreationForm
from freearticleapp.models import FreeArticle


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleCreationForm
    template_name = 'articleapp/create.html'

    def form_valid(self, form):
        form.instance.writer = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.pk})


class ArticleDetailView(DetailView, FormMixin):
    model = Article
    context_object_name = 'target_article'
    form_class = CommentCreationForm
    template_name = 'articleapp/detail.html'

    def get(self, request, *args, **kwargs):

        clicked_article = Article.objects.get(pk=kwargs['pk'])
        clicked_article.hits += 1
        clicked_article.save()
        print(clicked_article.hits)
        return super().get(request, *args, **kwargs)


@method_decorator(article_ownership_required, 'get')
@method_decorator(article_ownership_required, 'post')
class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleCreationForm
    context_object_name = 'target_article'
    template_name = 'articleapp/update.html'

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.pk})


@method_decorator(article_ownership_required, 'get')
@method_decorator(article_ownership_required, 'post')
class ArticleDeleteView(DeleteView):
    model = Article
    context_object_name = 'target_article'
    success_url = reverse_lazy('articleapp:list_all')
    template_name = 'articleapp/delete.html'


class ArticleListView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'articleapp/list.html'
    paginate_by = 20


class SearchFormView(FormView):
    form_class = PostSearchForm
    template_name = 'articleapp/post_search.html'

    def form_valid(self, form):
        searchWord = form.cleaned_data['search_word']
        post_list = Article.objects.filter(Q(title__icontains=searchWord) | Q(content__icontains=searchWord) | Q(writer__username__icontains=searchWord)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = post_list

        return render(self.request, self.template_name, context)


class ArticleListView1(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'articleapp/list_language_study.html'
    paginate_by = 20


class ArticleListView2(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'articleapp/list_employment.html'
    paginate_by = 20


class ArticleListView3(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'articleapp/list_public_officer.html'
    paginate_by = 20


class ArticleListView4(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'articleapp/list_hobby.html'
    paginate_by = 20


class ArticleListView5(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'articleapp/list_programming.html'
    paginate_by = 20


class ArticleListView6(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'articleapp/list_other.html'
    paginate_by = 20


class ArticleHomeView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'articleapp/home.html'

    def get_queryset(self):
        return Article.objects.order_by('-created_at')[:5]

    def get_context_data(self, **kwargs):
        article_free_list = FreeArticle.objects.all()
        return super().get_context_data(article_free_list=article_free_list,
                                        **kwargs)



