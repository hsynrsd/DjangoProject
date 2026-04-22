from itertools import product

from django.shortcuts import render
from django.http import HttpResponse

from shop.models import Product


def home(request):
    products = Product.objects.all()

    contextData = {"shopName": "Django Ice cream Shop","companyName": "IMC ICE", "products": {"ice_cream_products": Product.objects.all() }}
    return render(request, "shop/index.html", context = contextData)

def about(request):
    return render(request, "shop/about.html")

def cart(request):
    return render(request, "shop/cart.html")