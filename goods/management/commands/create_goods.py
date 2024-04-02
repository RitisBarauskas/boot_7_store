import random

from django.core.management import BaseCommand

from goods.factories import GoodFactory, AuthorFactory, CategoryFactory


class Command(BaseCommand):
    help = 'Create goods'

    def add_arguments(self, parser):
        parser.add_argument('author_count', type=int, default=10)
        parser.add_argument('category_count', type=int, default=10)
        parser.add_argument('goods_count', type=int, default=100)

    def handle(self, *args, **options):
        authors = AuthorFactory.create_batch(options['author_count'])
        categories = CategoryFactory.create_batch(options['category_count'])

        for author in authors:
            for _ in range(options['goods_count']):
                current_categories = random.choices(categories, k=random.randint(1, 5))
                GoodFactory.create(author=author, categories=current_categories)
            self.stdout.write(self.style.SUCCESS(f'Goods created for {author.name}'))

        self.stdout.write(self.style.SUCCESS('Goods created successfully'))