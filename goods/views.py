from django.shortcuts import render, get_object_or_404

from .constants import MAX_OBJECTS_ON_PAGE
from .helpers import query_debugger
from .models import Author, Good, Category


@query_debugger
def index(request):
    goods = Good.objects.select_related('author').prefetch_related('categories')[:MAX_OBJECTS_ON_PAGE]
    return render(request, 'goods/index.html', {'goods': goods})


@query_debugger
def good_detail(request, id):
    good = get_object_or_404(Good.objects.select_related('author').prefetch_related('categories'), pk=id)

    return render(request, 'goods/detail.html', {'good': good})


@query_debugger
def goods_of_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    goods = category.goods.select_related('author').prefetch_related('categories')[:MAX_OBJECTS_ON_PAGE]

    return render(request, 'goods/index.html', {'goods': goods})


@query_debugger
def goods_of_author(request, id):
    author = get_object_or_404(Author, pk=id)
    goods = author.goods.prefetch_related('categories')[:MAX_OBJECTS_ON_PAGE]

    return render(request, 'goods/index.html', {'goods': goods})
