from django.urls import path

from .views import (
    index,
    good_detail,
    goods_of_category,
    goods_of_author,
    CategoryCreateView,
    GoodCreateView,
    AuthorCreateView,
)

app_name = 'goods'

urlpatterns = [
    path('category/create/', CategoryCreateView.as_view(), name='category_create'),
    path('good/create/', GoodCreateView.as_view(), name='good_create'),
    path('author/create/', AuthorCreateView.as_view(), name='author_create'),
    path('category/<slug:slug>/', goods_of_category, name='category'),
    path('author/<int:id>/', goods_of_author, name='author'),
    path('<int:id>/', good_detail, name='detail'),
    path('', index, name='index'),

]
