from django.urls import path

from .views import index, good_detail, goods_of_category, goods_of_author

app_name = 'goods'

urlpatterns = [
    path('', index, name='index'),
    path('<int:id>/', good_detail, name='detail'),
    path('category/<slug:slug>/', goods_of_category, name='category'),
    path('author/<int:id>/', goods_of_author, name='author'),
]
