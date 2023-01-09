from .serializer import ProductSerializer, CategorySerializer
from store.models import Category, Product
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProductFilter


# from urllib import response
# from django.shortcuts import render, get_object_or_404
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.views import APIView
# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class ProductsViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ['name', 'description']
    ordering_fields = ['old_price']
    pagenation_class = PageNumberPagination

    # def get(self, requset):
    #     products = Product.objects.all()
    #     serializer = ProductSerializer(products, many=True)
    #     return Response(serializer.data)

    # def post(self, request):
    #     serializer = ProductSerializer(data=request.data)   
    #     serializer.is_valid(raise_exception=True)     
    #     serializer.save()
    #     return Response(serializer.data)




# class ApiProduct(RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


    # def get(self, requset, pk):
    #     product = get_object_or_404(Product, id=pk)
    #     serializer = ProductSerializer(product)
    #     return Response(serializer.data)

    # def put(self, request, pk):
    #     product = get_object_or_404(Product, id=pk)
    #     serializer = ProductSerializer(product, data=request.data)   
    #     serializer.is_valid(raise_exception=True)     
    #     serializer.save()
    #     return Response(serializer.data)

    # def delete(self, request, pk):
    #     product = get_object_or_404(Product, id=pk)
    #     product.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)



class CategoriesViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    # def get(self, requset):
    #     category = Category.objects.all()
    #     serializer = CategorySerializer(category, many=True)
    #     return Response(serializer.data)

    # def post(self, request):
    #     serializer = CategorySerializer(data=request.data)   
    #     serializer.is_valid(raise_exception=True)     
    #     serializer.save()
    #     return Response(serializer.data)



# class ApiCategory(RetrieveUpdateDestroyAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

    # def get(self, requset, pk):
    #     category = get_object_or_404(Category, category_id=pk)
    #     serializer = CategorySerializer(category)
    #     return Response(serializer.data)

    # def put(self, request, pk):
    #     category = get_object_or_404(Category, category_id=pk)
    #     serializer = CategorySerializer(category, data=request.data)   
    #     serializer.is_valid(raise_exception=True)     
    #     serializer.save()
    #     return Response(serializer.data)

    # def delete(self, request, pk):
    #     category = get_object_or_404(Category, category_id=pk)
    #     category.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


