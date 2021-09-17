from datetime import datetime, timezone, timedelta

from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class FreeArticle(models.Model):

    writer = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='freearticle')
    title = models.CharField(max_length=200, verbose_name='제목')
    image = models.ImageField(upload_to='article/', null=True)
    content = models.TextField(verbose_name='글 내용')
    created_at = models.DateTimeField(auto_now_add=True)
    hits = models.PositiveIntegerField(default=0, verbose_name='조회수')

    class Meta:
        ordering = ['-created_at']

    def created_string(self):
        now = datetime.now(tz=timezone.utc)

        time = now - self.created_at
        if time < timedelta(minutes=1):
            return '방금 전'
        elif time < timedelta(hours=1):
            return str(int(time.seconds / 60)) + '분 전'
        elif time < timedelta(days=1):
            return str(int(time.seconds / 3600)) + '시간 전'

        time = now.date() - self.created_at.date()
        if time < timedelta(weeks=1):
            return str(time.days) + '일 전'
        elif time < timedelta(weeks=4):
            return str(int(time.days / 7)) + '주 전'
        elif time < timedelta(weeks=52):
            return str(int(time.days / 30)) + '개월 전'

        return str(int(time.days / 365)) + '년 전'
