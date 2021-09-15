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

    def get_queryset(self):
        category = self.kwargs['category']
        if category == 'all':
            result = Article.objects.all()
        else:
            # 1. 애초에 form 에서 전송할 때, 변환되서 오면 안되나?
            # 2. 데이터베이스에 String으로 저장되어야 하는 이유라도?
            #    (0, 1, 2, 3, 4, ... 같이 숫자로 저장하면 안됨?)
            if category == 'lang':
                category = '어학'
            elif category == 'employ':
                category = '취업'
            elif category == 'public':
                category = '고시/공무원'
            elif category == 'hobby':
                category = '취미/교양'
            elif category == 'coding':
                category = '프로그래밍'
            elif category == 'etc':
                category = '기타'

            result = Article.objects.filter(progress_method=category)
        return result


# FormView 를 상속받게 해놨던데, 무슨 이유라도?
# 검색결과 화면은 ListView 아닌가?
class SearchFormView(ListView):
    form_class = PostSearchForm
    context_object_name = 'article_list'
    template_name = 'articleapp/list.html'

    # 몇 가지 질문 사항
    # 1. form 유효성 검사하는 form_valid() 함수에서 검색 결과 조회하고 render 해주는데, 이거 맞아?
    #    함수가 본인의 역할 이상의 일을 수행하고 있는거 아니야?
    # 2. 단순 데이터 요청인데 굳이 form 으로 post 요청을 하는 이유는?
    #   2.1. get 과 post 는 뭐고, 어떨때 사용하는지? (http method!!)

    # def form_valid(self, form):
    #     searchWord = form.cleaned_data['search_word']
    #     post_list = Article.objects.filter(
    #         Q(title__icontains=searchWord) | Q(content__icontains=searchWord) | Q(writer__username__icontains=searchWord)
    #     ).distinct()
    #
    #     context = {}
    #     context['form'] = form
    #     context['search_term'] = searchWord
    #     context['object_list'] = post_list
    #
    #     return render(self.request, self.template_name, context)

    def get_queryset(self):
        search_key = self.request.GET['search_word']

        post_list = Article.objects.filter(
            Q(title__icontains=search_key) | Q(content__icontains=search_key) | Q(writer__username__icontains=search_key)
        ).distinct()

        return post_list


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



