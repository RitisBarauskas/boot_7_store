# import random
#
# from django.test import TestCase
# from django.contrib.auth import get_user_model
# from django.test import Client
# from django.urls import reverse
#
# from goods.constants import MAX_OBJECTS_ON_PAGE
# from goods.models import Good, Author
#
# User = get_user_model()
#
#
# class TestGoods(TestCase):
#     @classmethod
#     def setUpClass(cls) -> None:
#         print("setUpClass")
#         super().setUpClass()
#         authors = [Author(name=f'Author {i}', age=50) for i in range(MAX_OBJECTS_ON_PAGE+1)]
#         Author.objects.bulk_create(authors)
#         cls.authors = Author.objects.all()
#         cls.creator = User.objects.create_user(username='test_user', password='12345', is_staff=True, is_active=True, is_superuser=True, email='some@email.com')
#         goods = [Good(title=f'Good {i}', description=f'Description {i}', creator=cls.creator, author=cls.authors[i]) for i in range(MAX_OBJECTS_ON_PAGE+1)]
#         Good.objects.bulk_create(goods)
#         cls.goods = Good.objects.all()
#
#     @classmethod
#     def tearDownClass(cls) -> None:
#         print("tearDownClass")
#         # cls.creator.delete()
#
#         super().tearDownClass()
#
#     def setUp(self) -> None:
#         super().setUp()
#         print("setUp")
#         self.creator_client = Client()
#         self.creator_client.force_login(self.creator)
#
#     def tearDown(self) -> None:
#         super().tearDown()
#         print("tearDown")
#
#     def test_index(self):
#         """
#         Тест проверки контекста на главной странице.
#         :return:
#         """
#         request = self.client.get(reverse('goods:index'))
#         self.assertIn('goods', request.context)
#         goods_context = request.context['goods']
#         self.assertLessEqual(goods_context.count(), MAX_OBJECTS_ON_PAGE)
#         goods = Good.objects.order_by('-created_at')
#         context_good = goods_context[0]
#         expected_good = goods[0]
#         self.assertEqual(context_good, expected_good)
#         self.assertEqual(expected_good.title, context_good.title)
#         self.assertEqual(expected_good.description, context_good.description)
#         self.assertEqual(expected_good.creator, context_good.creator)
#         self.assertEqual(expected_good.author, context_good.author)
#
#     def test_new_good_on_first_position(self):
#         """
#         Тест проверки нового товара на первой позиции.
#         :return:
#         """
#         request_before = self.client.get(reverse('goods:index'))
#         good = Good.objects.create(title='New Good', description='New Description', creator=self.creator, author=self.authors[0])
#         request = self.client.get(reverse('goods:index'))
#         goods_context = request.context['goods']
#         self.assertEqual(goods_context[0], good)
#         self.assertEqual(request_before.context['goods'][0], goods_context[1])
#
#     def test_detail(self):
#         print("test_movie_detail")
#
#     def test_good_create(self):
#         print("test_good_create")
#
#     def test_category_create(self):
#         print("test_category_create")
#
