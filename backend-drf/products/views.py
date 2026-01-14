from django.shortcuts import render
from rest_framework import generics
from .models import Product
from.serializers import ProductSerializers
# Create your views here.

class ProductListView(generics.ListAPIView):
    queryset= Product.objects.filter(is_active=True)
    serializer_class= ProductSerializers
    
class ProductDetailView(generics.RetrieveAPIView):
    queryset= Product.objects.filter(is_active=True)
    serializer_class= ProductSerializers
    
    