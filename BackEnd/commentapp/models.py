from datetime import datetime, timezone, timedelta

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from articleapp.models import Article
from freearticleapp.models import FreeArticle


class Comment(models.Model):

    article = models.ForeignKey(Article, on_delete=models.SET_NULL,
                                related_name='comments', null=True)

    freearticle = models.ForeignKey(FreeArticle, on_delete=models.SET_NULL,
                                related_name='free_comments', null=True)

    writer = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='comments')
    content = models.TextField()
    secret = models.BooleanField(default=False)
    parent = models.ForeignKey('self', on_delete=models.CASCADE,
                               null=True, blank=True, related_name='replies')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('create_at', )

    @property
    def children(self):
        return Comment.objects.filter(parent=self).order_by('create_at').all()

    @property
    def is_parent(self):
        if self.parent is None:
            return True
        return False

    @property
    def created_string(self):
        now = datetime.now(tz=timezone.utc)

        time = now - self.create_at
        if time < timedelta(minutes=1):
            return '방금 전'
        elif time < timedelta(hours=1):
            return str(int(time.seconds / 60)) + '분 전'
        elif time < timedelta(days=1):
            return str(int(time.seconds / 3600)) + '시간 전'

        time = now.date() - self.create_at.date()
        if time < timedelta(weeks=1):
            return str(time.days) + '일 전'
        elif time < timedelta(weeks=4):
            return str(int(time.days / 7)) + '주 전'
        elif time < timedelta(weeks=52):
            return str(int(time.days / 30)) + '개월 전'

        return str(int(time.days / 365)) + '년 전'

