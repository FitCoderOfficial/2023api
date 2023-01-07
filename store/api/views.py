from urllib import response
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from .serializer import ProductSerializer, CategorySerializer
from store.models import Category, Product
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView



class ApiProducts(APIView):
    def get(self, requset):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)   
        serializer.is_valid(raise_exception=True)     
        serializer.save()
        return Response(serializer.data)

class ApiProduct(APIView):
    def get(self, requset, pk):
        product = get_object_or_404(Product, id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        serializer = ProductSerializer(product, data=request.data)   
        serializer.is_valid(raise_exception=True)     
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class ApiCategories(APIView):
    def get(self, requset):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)   
        serializer.is_valid(raise_exception=True)     
        serializer.save()
        return Response(serializer.data)

class ApiCategory(APIView):
    def get(self, requset, pk):
        category = get_object_or_404(Category, category_id=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, pk):
        category = get_object_or_404(Category, category_id=pk)
        serializer = CategorySerializer(category, data=request.data)   
        serializer.is_valid(raise_exception=True)     
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        category = get_object_or_404(Category, category_id=pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


