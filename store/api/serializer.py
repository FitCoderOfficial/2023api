from itertools import product
from rest_framework import serializers
from store.models import Category, Product



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["category_id", "title", "slug"]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [ "id", "name", 'image', "description", "category", "slug", "inventory", "old_price", "price", "top_deal", "flash_sales"]

    category = CategorySerializer()
    #category = serializers.StringRelatedField()


