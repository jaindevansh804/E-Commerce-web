from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=90)
    category = models.CharField(max_length=90)
    price = models.IntegerField()
    description = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to="shop/images")
    
    def __str__(self):
        return self.name
    
class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    mobile = models.IntegerField()
    subject = models.CharField(max_length=150)
    message = models.TextField()

    def __str__(self):
        return self.name

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=1000)
    email = models.EmailField(max_length=500)
    addressline1 = models.TextField()
    addressline2 = models.TextField()
    city = models.CharField(max_length=500)
    state = models.CharField(max_length=200)
    zip_code = models.IntegerField()
    phone = models.IntegerField()

    def __str__(self):
        return "You received new order from" + self.name

