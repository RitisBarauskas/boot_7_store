import random

import factory
from factory.django import DjangoModelFactory

from .enums import ProductTypeEnum
from .models import Author, Category, Good


class AuthorFactory(DjangoModelFactory):
    class Meta:
        model = Author

    name = factory.Faker('name')
    age = factory.Faker('random_int', min=16, max=100)
    country = factory.Faker('country')


class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category

    title = factory.Faker('word')
    slug = factory.Faker('slug')
    description = factory.Faker('text')


class GoodFactory(DjangoModelFactory):
    class Meta:
        model = Good

    title = factory.Faker('word', locale='ru_RU')
    description = factory.Faker('text')
    product_type = None

    @classmethod
    def _create(cls, model_class, *args, categories=None, author=None, **kwargs):
        if not kwargs.get('product_type'):
            kwargs['product_type'] = random.choice(ProductTypeEnum.choices())[0]

        if author is None:
            raise ValueError('Author must be specified')

        kwargs['author'] = author

        if categories is None:
            raise ValueError('Categories must be specified')

        item = super()._create(model_class, *args, **kwargs)

        item.categories.set(categories)

        return item
