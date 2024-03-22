from django.shortcuts import render, get_object_or_404

from .models import Author, Good, Category


def index(request):
    goods = Good.objects.all()
    return render(request, 'goods/index.html', {'goods': goods})


def good_detail(request, id):
    good = get_object_or_404(Good, pk=id)

    return render(request, 'goods/detail.html', {'good': good})


def goods_of_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    goods = category.goods.all()

    return render(request, 'goods/index.html', {'goods': goods})


def goods_of_author(request, id):
    author = get_object_or_404(Author, pk=id)
    goods = author.goods.all()

    return render(request, 'goods/index.html', {'goods': goods})
