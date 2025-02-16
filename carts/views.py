from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import JsonResponse

from main.models import Product
from users.models import User
from carts.models import Cart


def cart_add(request, product_slug):
    """Добавление в корзину пользователем и также анонимным пользователем"""
    product = Product.objects.get(slug=product_slug)
    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product=product)
        if not carts.exists():
            cart = Cart.objects.create(user=request.user, product=product, quantity=1)
            return HttpResponseRedirect(request.META['HTTP_REFERER'])  # Перевод на текущую страницу
        else:
            cart = carts.first()
            cart.quantity += 1
            cart.save()
            return HttpResponseRedirect(request.META['HTTP_REFERER'])  # Перевод на текущую страницу
    else:   # Если Юзер не authenticated
        carts = Cart.objects.filter(session_key=request.session.session_key, product=product)
        if not carts.exists():
            cart = Cart.objects.create(session_key=request.session.session_key, product=product, quantity=1)
            return HttpResponseRedirect(request.META['HTTP_REFERER'])  # Перевод на текущую страницу
        else:
            cart = carts.first()
            cart.quantity += 1
            cart.save()
            return HttpResponseRedirect(request.META['HTTP_REFERER'])  # Перевод на текущую страницу


def cart_change(request, product_slug):
    """Изменение количества товара в корзине"""
    if request.method == 'POST':
        action = request.POST.get('action')
        cart_id = request.POST.get('cart_id')
        cart = Cart.objects.get(id=cart_id)

        # Инициализация переменных
        total_quantity = 0
        total_price = 0.0

        if action == 'increment':
            cart.quantity += 1
        elif action == 'decrement':
            if cart.quantity > 1:  # Не позволяем уменьшать количество ниже 1
                cart.quantity -= 1

        cart.save()

        # Пересчитываем общее количество и цену
        all_carts = Cart.objects.filter(user=request.user)  # Замените на метод получения корзины пользователя
        for item in all_carts:
            total_quantity += item.quantity
            total_price += item.products_price  # Или item.product.price * item.quantity в зависимости от вашей модели

        return JsonResponse({
            'new_quantity': cart.quantity,
            'total_quantity': total_quantity,
            'total_price': total_price,
        })

def cart_remove(request, cart_id):
    """Удаление товара из корзины (удаление корзины)"""
    cart = Cart.objects.get(id=cart_id)
    cart.delete()
    return redirect(request.META['HTTP_REFERER'])