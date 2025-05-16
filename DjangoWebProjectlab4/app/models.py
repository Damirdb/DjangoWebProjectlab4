"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from datetime import datetime
from django.urls import reverse

class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    short_content = models.TextField(verbose_name="Краткое содержание")
    full_content = models.TextField(verbose_name="Полное содержание")
    posted = models.DateTimeField(default=datetime.now, verbose_name="Опубликована")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="Автор")
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True, verbose_name="Изображение")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Статья блога"
        verbose_name_plural = "Статьи блога"
        ordering = ["-posted"]

class Comment(models.Model):
    post = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name="Статья"
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Автор"
    )
    text = models.TextField(verbose_name="Текст комментария")
    date = models.DateTimeField(default=datetime.now, verbose_name="Дата комментария")

    def __str__(self):
        return f"Комментарий от {self.author} к статье '{self.post.title}'"

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ["-date"]

admin.site.register(Blog)
admin.site.register(Comment)
