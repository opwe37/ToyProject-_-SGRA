from datetime import datetime, timezone, timedelta

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Article(models.Model):

    writer = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='article')
    title = models.CharField(max_length=200, verbose_name='제목')
    image = models.ImageField(upload_to='article/', null=True)
    content = models.TextField(verbose_name='글 내용')
    created_at = models.DateTimeField(auto_now_add=True)

    NATIONAL_CHOICES1 = (
        ('서울특별시', '서울특별시'),
        ('경기도', '경기도'),
        ('강원도', '강원도'),
        ('충청도', '충청도'),
        ('전라도', '전라도'),
        ('경상도', '경상도'),
        ('제주도', '제주도')
    )

    NATIONAL_CHOICES2 = (
        ('어학', '어학'),
        ('취업', '취업'),
        ('고시/공무원', '고시/공무원'),
        ('취미/교양', '취미/교양'),
        ('프로그래밍', '프로그래밍'),
        ('기타', '기타')
    )

    NATIONAL_CHOICES3 = (
        ('상관없음', '상관없음'),
        ('1~2명', '1~2명'),
        ('3~4명', '3~4명'),
        ('5~6명', '5~6명'),
        ('6명이상', '6명이상')
    )

    region = models.CharField(max_length=10, choices=NATIONAL_CHOICES1, default=True, verbose_name='지역')
    progress_method = models.CharField(max_length=10, choices=NATIONAL_CHOICES2, default=True, verbose_name='분야')
    max_personnel = models.CharField(max_length=10, choices=NATIONAL_CHOICES3, default=True, verbose_name='최대 인원 수')
    hits = models.PositiveIntegerField(default=0, verbose_name='조회수')

    class Meta:
        ordering = ['-created_at']

    @property
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
