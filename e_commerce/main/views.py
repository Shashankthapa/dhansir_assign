
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def shop(request):
    return render(request,'shop.html')

def shop_details(request):
    return render(request, 'shop_details.html')

def shop_cart(request):
    return render(request, 'shop_cart.html')