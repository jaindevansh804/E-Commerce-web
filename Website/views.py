from django.shortcuts import render, HttpResponse
from Website.models import Products, Contact

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

def productview(request, name):
    # To get the products by filtering add .first after fetching from database
    allproducts = Products.objects.filter(name=name).first()
    # All the products will be fetched using filters. They will have a additional extension of url in urls.py with may be either str, id, etc .
    prod = {'allproducts': allproducts}
    return render(request, 'productview.html', prod)


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        details = Contact(name=name, email=email, mobile=mobile, subject=subject, message=message)
        details.save()
    return render(request, 'contact.html')