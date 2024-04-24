from rest_framework import viewsets

from goods.models import Good, Category, Author
from .serializers import GoodReadSerializer, GoodWriteSerializer, CategorySerializer, AuthorSerializer


class GoodViewSet(viewsets.ModelViewSet):

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return GoodReadSerializer
        return GoodWriteSerializer

    def get_queryset(self):
        return Good.objects.select_related(
            'author',
        ).prefetch_related(
            'categories',
        ).order_by('author__name', 'id')


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
