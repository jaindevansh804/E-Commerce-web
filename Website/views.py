from django.shortcuts import render, HttpResponse
from Website.models import Products

# The name of the project is Website


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def shop(request):
    allproducts = Products.objects.all()
    prod = {'allproducts':allproducts}
    return render(request, 'shop.html', prod)

def contact(request):
    return render(request, 'contact.html')