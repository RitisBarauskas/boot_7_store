import random

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .constants import MAX_OBJECTS_ON_PAGE
from .helpers import query_debugger
from .models import Author, Good, Category
from .forms import GoodForm, CategoryForm, AuthorForm


# @query_debugger
def index(request):
    goods = Good.objects.select_related('author').prefetch_related('categories').order_by('-created_at')[:MAX_OBJECTS_ON_PAGE]
    return render(request, 'goods/index.html', {'goods': goods})


# @query_debugger
def good_detail(request, id):
    good = get_object_or_404(Good.objects.select_related('author').prefetch_related('categories'), pk=id)

    return render(request, 'goods/detail.html', {'good': good})


# @query_debugger
def goods_of_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    goods = category.goods.select_related('author').prefetch_related('categories')[:MAX_OBJECTS_ON_PAGE]

    return render(request, 'goods/index.html', {'goods': goods})


# @query_debugger
def goods_of_author(request, id):
    author = get_object_or_404(Author, pk=id)
    goods = author.goods.prefetch_related('categories')[:MAX_OBJECTS_ON_PAGE]

    return render(request, 'goods/index.html', {'goods': goods})


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'goods/category_form.html'
    success_url = reverse_lazy('goods:index')


class GoodCreateView(LoginRequiredMixin, CreateView):
    model = Good
    form_class = GoodForm
    template_name = 'goods/good_form.html'
    success_url = reverse_lazy('goods:index')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'goods/author_form.html'
    success_url = reverse_lazy('goods:index')

