from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Article(models.Model):

    writer = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='freearticle')
    title = models.CharField(max_length=200 ,verbose_name='제목')
    image = models.ImageField(upload_to='article/', null=True)
    content = models.TextField(verbose_name='글 내용')
    created_at = models.DateTimeField(auto_now_add=True)
    hits = models.PositiveIntegerField(default=0, verbose_name='조회수')

    class Meta:
        ordering = ['-created_at']