from urllib import response
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from .serializer import ProductSerializer, CategorySerializer
from store.models import Category, Product
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

@api_view(['GET', 'POST'])
def api_products(request):
    if request.method == 'GET':
         products = Product.objects.all()
         serializer = ProductSerializer(products, many=True)
         return Response(serializer.data)
   
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        
        serializer.save()
        # else:
        #     Response(serializer.errors)
        return Response(serializer.data)
        


@api_view(['GET', 'PUT'])
def api_product(request, pk):
    product = get_object_or_404(Product, id=pk)
    if request.method == 'GET':        
        serializer = ProductSerializer(product)
        return Response(serializer.data)
        
  
    if request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()        
        # else:
        #     Response(serializer.errors)
        return Response(serializer.data)
        


@api_view()
def api_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view()
def api_category(request, pk):
    category = get_object_or_404(Category, category_id=pk)
    serializer = CategorySerializer(category)
    return Response(serializer.data)