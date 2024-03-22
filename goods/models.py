from django.db import models

from .constants import MAX_LENGTH_CHAR_FIELD
from .enums import ProductTypeEnum


class Author(models.Model):
    name = models.CharField('Имя', max_length=MAX_LENGTH_CHAR_FIELD)
    age = models.IntegerField('Возраст')
    country = models.CharField('Страна', max_length=MAX_LENGTH_CHAR_FIELD)

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return self.name


class Category(models.Model):
    title = models.CharField('Название', max_length=MAX_LENGTH_CHAR_FIELD)
    slug = models.SlugField('Слаг', unique=True)
    description = models.TextField('Описание', blank=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Good(models.Model):
    title = models.CharField('Название', max_length=MAX_LENGTH_CHAR_FIELD)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Автор', related_name='goods')
    categories = models.ManyToManyField(Category, verbose_name='Категории', related_name='goods')
    description = models.TextField('Описание', blank=True)
    product_type = models.CharField(
        'Тип продукта',
        max_length=MAX_LENGTH_CHAR_FIELD,
        choices=ProductTypeEnum.choices(),
    )
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.title
