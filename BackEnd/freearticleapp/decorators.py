from django.http import HttpResponseForbidden

from freearticleapp.models import FreeArticle


def article_ownership_required(func):
    def decorated(request, *args, **kwargs):
        target_article = FreeArticle.objects.get(pk=kwargs['pk'])
        if target_article.writer == request.user:
            return func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()
    return decorated