from django.db import models
import uuid
from phonenumber_field.modelfields import PhoneNumberField


class Author(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField('Имя', max_length=255, unique=False)
    phone = PhoneNumberField('Телефон', region='RU', unique=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Genre(models.Model):
    title = models.CharField('Название жанра', max_length=255, unique=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Books(models.Model):
    title = models.CharField('Название', max_length=255, unique=False)
    author = models.ManyToManyField(Author, blank=True, related_name='authors')
    genre = models.ManyToManyField(Genre, blank=True, related_name='authors')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
