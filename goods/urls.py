from django.urls import path

from .views import index, detail

app_name = 'goods'

urlpatterns = [
    path('', index, name='index'),
    path('<int:id>/', detail, name='detail'),
]
