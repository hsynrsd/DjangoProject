from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from Shop_Project1 import settings
from shop import views

urlpatterns = [
    path('', views.home, name="shop-page"),
    path('about/', views.about, name="about-page"),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('contact/', views.contact_page, name='contact_page'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)