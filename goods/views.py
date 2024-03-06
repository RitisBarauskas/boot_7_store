from django.http import Http404
from django.shortcuts import render

from .constants import GOODS


def index(request):
    return render(request, 'goods/index.html', {'goods': GOODS})


def detail(request, id):
    good = next((good for good in GOODS if good['id'] == id), None)
    if not good:
        raise Http404()

    return render(request, 'goods/detail.html', {'good': good})
