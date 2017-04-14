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

def product(request, id):
    template = 'product.html'
    context = {
        'product': Product.objects.get(id=id)
    }
    return render(context, request)
