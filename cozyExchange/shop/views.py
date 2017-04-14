from django.shortcuts import render

from .models import *

def home(request):
    context = {
        'categories': Category.objects.all(),
    }
    template = 'home.html'
    return render(request, template, context)

def about(request):
    context = {}
    template = 'about.html'
    return render(request, template, context)

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    template = 'product.html'
    context = {
        'category': category,
        'categories': categories,
        'products': products,
    }
    return render(context, request)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    template = 'product.html'
    context = {
        'product': product,
        'cart_product_form': cart_product_form
    }
    return render(context, request)
