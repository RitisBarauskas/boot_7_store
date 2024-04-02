from django.core.management import BaseCommand

from goods.factories import AuthorFactory


class Command(BaseCommand):
    help = 'Create authors'

    def handle(self, *args, **options):
        AuthorFactory.create_batch(10)
