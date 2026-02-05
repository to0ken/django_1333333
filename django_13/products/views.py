from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Category, Product


def product_list(request, category_slug=None):
    """Отображает список товаров (всех или по категории)"""
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    return render(request, 'products/product/list.html', {
        'category': category,
        'categories': categories,
        'products': products
    })


def product_detail(request, id, slug):
    """Отображает детальную информацию о товаре"""
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'products/product/detail.html', {'product': product})