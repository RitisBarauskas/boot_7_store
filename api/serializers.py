from rest_framework import serializers

from goods.models import Good, Category, Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class GoodReadSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    categories = CategorySerializer(many=True)
    aname = serializers.SerializerMethodField()

    class Meta:
        model = Good
        fields = '__all__'

    def get_aname(self, obj):
        return obj.author.name


class GoodWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Good
        fields = ('description', 'title', 'author', 'categories', 'product_type')

    def to_representation(self, instance):
        return GoodReadSerializer(instance).data
