from django.contrib import admin

from .models import Author, Category, Good


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Good)
class GoodAdmin(admin.ModelAdmin):
    pass
