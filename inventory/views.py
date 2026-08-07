from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from .models import Product,Supplier,Category

from .serializers import(ProductSerializer,SupplierSerializer,CategorySerializer)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class =CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class = ProductSerializer


class SupplierViewSet(viewsets.ModelViewSet):
    queryset=Supplier.objects.all()
    serializer_class= SupplierSerializer

def home(request):
    return render(request,"index.html")