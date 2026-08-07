from django.db import models

class Category(models.Model):
    name =models.CharField( max_length=50)

    def __str__(self):
        return self.name



class Supplier(models.Model):
    name = models.CharField( max_length=50)
    phone = models.CharField( max_length=50)


    def __str__(self):
        return self.name
    
    
class Product(models.Model):
    name=models.CharField( max_length=50)
    price = models.DecimalField( max_digits=10, decimal_places=2)
    quantity = models.DecimalField( max_digits=10, decimal_places=2)

    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

# Create your models here.
