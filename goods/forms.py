from django.forms import ModelForm

from .models import Good, Category, Author


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = '__all__'


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class GoodForm(ModelForm):
    class Meta:
        model = Good
        exclude = ('creator',)
