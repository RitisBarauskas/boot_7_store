import random

import pytest
from django.urls import reverse
from django.test import Client

from users.factories import UserFactory
from goods.factories import CategoryFactory, GoodFactory, AuthorFactory


@pytest.fixture
def moderator():
    return UserFactory(is_staff=True, is_superuser=True)


@pytest.fixture
def moderator_client(moderator):
    client = Client()
    client.force_login(moderator)
    return client


@pytest.fixture
def categories():
    return CategoryFactory.create_batch(10)


@pytest.fixture
def authors():
    return AuthorFactory.create_batch(10)


@pytest.fixture
def goods(categories, moderator, authors):
    for author in authors:
        GoodFactory.create_batch(10, author=author, creator=moderator, categories=random.choices(categories, k=3))


@pytest.fixture
def good(categories, moderator, authors):
    return GoodFactory.create(author=random.choice(authors), creator=moderator, categories=random.choices(categories, k=3))


@pytest.fixture
def detail_good_url(good):
    return reverse('goods:good_detail', kwargs={'id': good.id})


@pytest.fixture
def create_category():
    return reverse('goods:category_create')

@pytest.fixture
def create_good():
    return reverse('goods:good_create')


@pytest.fixture
def index_url():
    return reverse('goods:index')


class Some:
    def __init__(self, position=(int, int)):
        self.position = position
