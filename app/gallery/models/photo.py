from django.contrib.auth import get_user_model
from django.db import models


class Posts(models.Model):
    author = models.ForeignKey(
        to=get_user_model(),
        related_name='user_post',
        null=False,
        blank=False,
        verbose_name='Автор',
        on_delete=models.CASCADE
    )
    signature = models.TextField(
        max_length=1000,
        null=False,
        blank=False,
        verbose_name="Подпись"
    )
    photo = models.ImageField(
        null=False,
        blank=False,
        upload_to='photo',
        verbose_name='Фотогарфия'
    )
    favorites = models.ManyToManyField(
        to=get_user_model(),
        blank=True,
        verbose_name='Избранное',
        related_name='favorites'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации поста'
    )

    def __str__(self):
        return f'{self.author} - {self.signature}'