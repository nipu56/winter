from __future__ import unicode_literals
from django.utils.encoding import *
from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField('TITLE', max_length=50)  # 제목
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='별칭 단어 하나')  # 제목 별칭, 기본키 대용,
    description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text="부가 제목")  # 부가제목, 비워도 됨
    content = models.TextField('CONTENT')  # 내용
    create_date = models.DateTimeField('CREATE_DATE', auto_now_add=True)  # 생성날짜
    modify_date = models.DateTimeField('MODIFY_DATE', auto_now=True)  # 수정날짜

    class Meta:  # 파라미터
        verbose_name = 'post'  # 별칭 이름
        verbose_name_plural = 'posts'  # 별칭 이름 복수
        db_table = 'my_post'
        ordering = ('-modify_date',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=(self.slug,) )

    def get_previous_post(self):
        return self.get_previous_by_modify_date()

    def get_next_post(self):
        return self.get_next_by_modify_date()
