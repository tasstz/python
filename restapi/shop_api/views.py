from django.shortcuts import render
from rest_framework import generics
from .serializer import ProductSerializer
from .models import Product
from django.contrib.auth.mixins import LoginRequiredMixin

class ProductViewSet(generics.ListAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductAddView(LoginRequiredMixin, generics.CreateAPIView):
    #if request.user.is_authenticated():
        queryset = Product.objects.all()
        serializer_class = ProductSerializer
        raise_exception = True

class ProductDetailView(LoginRequiredMixin, generics.RetrieveUpdateDestroyAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    raise_exception = True
