from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Comment(models.Model):
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
