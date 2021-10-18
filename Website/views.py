from django.shortcuts import render, HttpResponse
from Website.models import Products, Contact, Order
from django.views.decorators.csrf import csrf_exempt
from PayTm import Checksum

MERCHANT_KEY = "G5#sU8Iu&M16kOTf"
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
        amount = request.POST.get('amount')
        name = request.POST.get('name')
        email = request.POST.get('email')
        addressline1 = request.POST.get('addressline1')
        addressline2 = request.POST.get('addressline2')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip_code')
        phone = request.POST.get('phone')
        order = Order(items_json=items_json, amount=amount, name=name, email=email, addressline1=addressline1, addressline2=addressline2, city=city, state=state, zip_code=zip_code, phone=phone)
        order.save()
        # return render(request, 'checkout.html', {'thank':thank})
    
        #request paytm to transfer the amount to your account after payment by user
        param_dict={

            'MID': 'SPTpoA80997673245579',
            'ORDER_ID': str(order.order_id),
            'TXN_AMOUNT': str(amount),
            'CUST_ID': email,
            'INDUSTRY_TYPE_ID': 'Retail',
            'WEBSITE': 'WEBSTAGING',
            'CHANNEL_ID': 'WEB',
            'CALLBACK_URL':'http://127.0.0.1:8000/handlerequest/',
        }
        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
        return render(request, "paytm.html", {'param_dict' : param_dict})
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

@csrf_exempt
def handlerequest(request):
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == "CHECKSUMHASH":
            checksum = form[i]

    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == "01":
            print('ORDER SUCCESSFUL')
        else:
            print('ORDER FAILURE. PLEASE TRY AGAIN' + response_dict['RESPMSG'])

    return render(request, 'paymentstatus.html', {'response':response_dict})