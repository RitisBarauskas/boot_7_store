from http import HTTPStatus

from goods.constants import MAX_OBJECTS_ON_PAGE
from goods.enums import ProductTypeEnum
from goods.factories import AuthorFactory, CategoryFactory
from goods.models import Good


def test_index(db, moderator, categories, client, index_url, goods):
    """
    Тест проверки контекста на главной странице
    """
    request = client.get(index_url)
    assert request.status_code == HTTPStatus.OK
    assert request.context['goods'].count() <= MAX_OBJECTS_ON_PAGE


def test_new_movie_first_position(db):
    """
    Тест проверки нового фильма на первой позиции.
    """


def test_create_category(db, client, create_category):
    """
    Тест создания категории.
    """


def test_create_good(db, moderator_client, create_good, goods, moderator):
    """
    Тест создания товара.
    """
    author = AuthorFactory()
    categories = CategoryFactory.create_batch(3)

    data = {
        'title': 'Test good',
        'description': 'Test description',
        'product_type': ProductTypeEnum.MOVIE.name,
        'author': author.id,
        'categories': [categories[0].id, categories[1].id, categories[2].id]
    }

    goods_before = set(Good.objects.all())

    request = moderator_client.post(create_good, data)
    assert request.status_code == HTTPStatus.FOUND

    goods_after = set(Good.objects.all())
    assert len(goods_after.difference(goods_before)) == 1

    good = goods_after.difference(goods_before).pop()

    assert good.title == data['title']
    assert good.description == data['description']
    assert good.product_type == data['product_type']
    assert good.author == author
    assert set(good.categories.all()) == set(categories)
    assert good.creator == moderator


def test_not_create_good_for_guest(db, client, create_good, goods, moderator):
    """
    Тест создания товара.
    """
    author = AuthorFactory()
    categories = CategoryFactory.create_batch(3)

    data = {
        'title': 'Test good',
        'description': 'Test description',
        'product_type': ProductTypeEnum.MOVIE.name,
        'author': author.id,
        'categories': [categories[0].id, categories[1].id, categories[2].id]
    }

    goods_before = set(Good.objects.all())

    request = client.post(create_good, data)
    assert request.status_code == HTTPStatus.FOUND

    goods_after = set(Good.objects.all())
    assert len(goods_after.difference(goods_before)) == 0
