from django.conf import settings
from django.db import models

from users.models import NULLABLE


class NewsPost(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    content = models.TextField(max_length=500, verbose_name='Содержимое')
    image = models.ImageField(upload_to='Wlog_image/', verbose_name='Изображение', **NULLABLE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    creation_date = models.DateField(auto_now=True, verbose_name='Дата создания поста')
    edition_date = models.DateTimeField(verbose_name='Дата изменения', default=creation_date)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return f'{self.title} {self.content} {self.author} {self.creation_date}'


class Comments(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(max_length=500, verbose_name='Содержимое')
    creation_date = models.DateField(auto_now=True, verbose_name='Дата создания комментария')
    edition_date = models.DateTimeField(verbose_name='Дата изменения', default=creation_date)
    post = models.ForeignKey(NewsPost, verbose_name='Пост', on_delete=models.CASCADE)
    related_comment = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='Связанный комментарий', **NULLABLE)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'{self.content} {self.author} {self.creation_date}'







