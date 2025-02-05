from django.shortcuts import render
from django.http import HttpResponse

from .models import Product, Category


# Create your views here.

def index(request):
    """Вывод главной страницы"""
    products = Product.objects.all()
    context = {'products': products, }
    return render(request, 'main/index.html', context=context)


def about(request):
    return HttpResponse('Это страница о нас')

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {'product': product}
    return render(request, 'main/product_detail.html', context=context)