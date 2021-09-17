from django.views.generic import ListView

from articleapp.models import Article
from freearticleapp.models import FreeArticle


class HomeView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'index.html'

    def get_queryset(self):
        return Article.objects.order_by('-created_at')[:5]

    def get_context_data(self, **kwargs):
        article_free_list = FreeArticle.objects.all()[:5]
        return super().get_context_data(article_free_list=article_free_list,
                                        **kwargs)
