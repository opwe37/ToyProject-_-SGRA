from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Article(models.Model):

    writer = models.ForeignKey(User, on_delete=models.SET_NULL,
                               related_name='article', null=True)
    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='article/', null=True)
    content = models.TextField(null=True)

    created_at = models.DateField(auto_now_add=True,null=True)

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
        ('전체', '전체'),
        ('어학', '어학'),
        ('취업', '취업'),
        ('고시/공무원', '고시/공무원'),
        ('취미/교양', '취미/교양'),
        ('프로그래밍', '프로그래밍'),
        ('기타', '기타')
    )

    NATIONAL_CHOICES3 = (
        ('상관없음','상관없음'),
        ('1~2명', '1~2명'),
        ('3~4명', '3~4명'),
        ('5~6명', '5~6명'),
        ('6명이상', '6명이상')
    )

    region = models.CharField(max_length=10, choices=NATIONAL_CHOICES1,default=True)

    progress_method = models.CharField(max_length=10, choices=NATIONAL_CHOICES2,default=True)

    max_personnel = models.CharField(max_length=10, choices=NATIONAL_CHOICES3,default=True)