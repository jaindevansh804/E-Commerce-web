from django.shortcuts import render, HttpResponse
from Website.models import Products, Contact, Order

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

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    if request.method=="POST":
        items_json = request.POST.get('itemsJson')
        name = request.POST.get('name')
        email = request.POST.get('email')
        addressline1 = request.POST.get('addressline1')
        addressline2 = request.POST.get('addressline2')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip_code')
        phone = request.POST.get('phone')
        order = Order(items_json=items_json, name=name, email=email, addressline1=addressline1, addressline2=addressline2, city=city, state=state, zip_code=zip_code, phone=phone)
        order.save()
        # If this order is true then thank will become true. then the javascipt will capture order from the user and send to database.
        thank = True
        return render(request, 'checkout.html', {'thank':thank})
    return render(request, 'checkout.html')

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