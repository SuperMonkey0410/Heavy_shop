from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator

from .models import Product, Category


# Create your views here.

def index(request, category_slug=None):
    """Вывод главной страницы + фильтрация по категориям"""
    category_list = Category.objects.all()
    if category_slug:
        categories = Category.objects.filter(slug=category_slug)
        products_list = Product.objects.filter(category__slug=category_slug)
    else:
        products_list = Product.objects.all()
        categories = Category.objects.all()

    paginator = Paginator(products_list, 6)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)
    context = {'products': products, 'categories': categories, 'category_list': category_list}
    return render(request, 'main/index.html', context=context)


def product_detail(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    categories = Category.objects.all()
    context = {'product': product, 'categories': categories}
    return render(request, 'main/product_detail.html', context=context)


