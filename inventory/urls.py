from rest_framework import routers
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet,CategoryViewSet,SupplierViewSet


routers = DefaultRouter()

routers.register("product",ProductViewSet)

routers.register("category",CategoryViewSet)

routers.register("supplier",SupplierViewSet)

urlpatterns = [
    path("",include(routers.urls))
]

