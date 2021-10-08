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