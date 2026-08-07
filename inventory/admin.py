from django.contrib import admin

from .models import Category,Product,Supplier

# Register your models here.
admin.site.register(Category)
admin.site.register(Supplier)
admin.site.register(Product)