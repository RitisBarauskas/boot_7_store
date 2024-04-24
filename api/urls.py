from django.urls import include, path
from rest_framework import routers

from api.views import GoodViewSet, CategoryViewSet, AuthorViewSet


router_v1 = routers.DefaultRouter()
router_v1.register('goods', GoodViewSet, basename='good')
router_v1.register('categories', CategoryViewSet, basename='category')
router_v1.register('authors', AuthorViewSet, basename='author')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
