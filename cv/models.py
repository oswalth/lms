from django.contrib import admin
from django.db import models
from django.utils.safestring import mark_safe


class Application(models.Model):
    name = models.CharField(max_length=128, verbose_name='Имя')
    email = models.EmailField(max_length=256, verbose_name='Email')
    image = models.ImageField(verbose_name='Изображение')
    snippet = models.TextField(verbose_name='Пример кода')
    first_email = models.BooleanField(default=False)
    second_email = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}, {self.email}"
