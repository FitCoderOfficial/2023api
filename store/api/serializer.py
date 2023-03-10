from itertools import product
from rest_framework import serializers
from store.models import Category, Product, Review, Cart, Cartitems, Banner


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ["title", "image"]


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



class SimpleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [ "id", "name", "price"]

class CartItemSerializer(serializers.ModelSerializer):
    product = SimpleProductSerializer(many=False)
    sub_total = serializers.SerializerMethodField(method_name='total')
    class Meta:
        model = Cartitems
        fields = ['id', 'cart', 'product', 'quantity', 'sub_total']

    def total(self, cartitem:Cartitems):
        return cartitem.quantity * cartitem.product.price

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)
    grand_total = serializers.SerializerMethodField(method_name='main_total')
    class Meta:
        model = Cart
        fields = ['owner', 'cart_id', 'created', 'completed', 'session_id', 'items', 'grand_total']

    def main_total(self, cart:Cart):
        items = cart.items.all()
        total = sum([item.quantity * item.product.price for item in items])
        return total 

    