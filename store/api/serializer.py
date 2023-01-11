from itertools import product
from rest_framework import serializers
from store.models import Category, Product, Review, Cart



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["category_id", "title", "slug"]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [ "id", "name", 'image', "description", "category", "slug", "inventory", "price", "top_deal", "flash_sales"]

    category = CategorySerializer()
    #category = serializers.StringRelatedField()

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'date_created', 'name', 'image', 'description']

    def create(self, validated_data):
        product_id = self.context["product_id"]
        return Review.objects.create(product_id=product_id, **validated_data)


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['owner', 'cart_id', 'created', 'completed', 'session_id', 'items']

    