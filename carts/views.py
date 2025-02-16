from django.shortcuts import render, redirect
from main.models import Product
from users.models import User
from carts.models import Cart


def cart_add(request, product_slug):
    """Добавление в корзину"""
    product = Product.objects.get(slug=product_slug)
    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product=product)

        if carts.exists():
            cart = carts.first()  # Или last без разницы.
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(user=request.user, product=product, quantity=1)
    return redirect(request.META['HTTP_REFERER'])

def cart_change(request, product_slug):
    """"""


def cart_remove(request, product_slug):
    """"""
