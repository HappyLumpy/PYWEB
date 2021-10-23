from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Note(models.Model):
    title = models.CharField(default='', max_length=200, verbose_name='Заголовок')
    massage = models.TextField(default='', verbose_name='Текст')
    date_add = models.DateTimeField(verbose_name='Дата публикции', default=datetime.now, blank=True)
    public = models.BooleanField(default=False, verbose_name='Публичный')
    author = models.ForeignKey(User, related_name='authors', on_delete=models.PROTECT, blank=True)

    def __str__(self):
        return self.title
