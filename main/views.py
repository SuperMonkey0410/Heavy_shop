from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Product, Category


# Create your views here.

def index(request):
    """Вывод главной страницы"""
    products = Product.objects.all()
    categories = Category.objects.all
    search = request.GET.get('q', None)
    context = {'products': products, 'categories': categories}
    return render(request, 'main/index.html', context=context)


def product_detail(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    categories = Category.objects.all()
    context = {'product': product, 'categories': categories}
    return render(request, 'main/product_detail.html', context=context)


def catalog(request, category_slug):
    products = Product.objects.filter(category__slug=category_slug)
    categories = Category.objects.all()
    category = Category.objects.get(slug=category_slug)
    context = {'products': products, 'categories': categories, 'category': category}
    return render(request, 'main/catalog.html', context=context)
