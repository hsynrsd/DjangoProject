from itertools import product

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product, Cart, CartItem, ContactMessage


from shop.models import Product


def home(request):
    products = Product.objects.all()

    user_cart = None
    if request.user.is_authenticated:
        # getattr(object, attr_name, default_value)
        # This returns None instead of crashing if the cart is missing
        user_cart = getattr(request.user, 'cart', None)

    contextData = {"sitename": "My Icecream Place",
                   "slogan": "So tasty!! hmmmm ",
                   "products": Product.objects.all(),
                   "cart": user_cart,
                   }
    return render(request, "shop/index.html", context = contextData)

def about(request):
    return render(request, "shop/about.html")


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # This creates the cart if it's missing, preventing the crash
    cart, created = Cart.objects.get_or_create(user=request.user)

    item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        item.quantity += 1
        item.save()

    return redirect('cart_detail')


@login_required
def remove_from_cart(request, product_id):
    # Safe retrieval: creates a cart if for some reason they don't have one
    cart, created = Cart.objects.get_or_create(user=request.user)
    product = get_object_or_404(Product, id=product_id)
    CartItem.objects.filter(cart=cart, product=product).delete()
    return redirect('cart_detail')


@login_required
def cart_detail(request):
    # If the user clicks "Cart" but never added anything,
    # this ensures the page loads with an empty cart instead of a 500 error.
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'shop/cart-detail.html', {'cart': cart})

@login_required
def contact_page(request):
    if request.method == "POST":
        msg_text = request.POST.get('message')
        if msg_text:
            ContactMessage.objects.create(user=request.user, message=msg_text)
            return redirect('contact_page')

    # Fetch all messages for this user to show the chat history
    chat_history = ContactMessage.objects.filter(user=request.user)
    return render(request, 'shop/contact.html', {'chat_history': chat_history})