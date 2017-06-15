from django.shortcuts import get_object_or_404, render

from .models import *

def home(request):
    context = {
        'categories': Category.objects.all(),
        'items': Item.objects.filter(available=True)
    }
    template = 'home.html'
    return render(request, template, context)

def about(request):
    context = {}
    template = 'about.html'
    return render(request, template, context)

def item_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    items = Item.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        items = items.filter(category=category)
    context = {
        'category': category,
        'categories': categories,
        'items': items,
    }
    return render(request, 'item/list.html', context)

#Change to listings
def item_detail(request, id, slug):
    item = get_object_or_404(Item, id=id, slug=slug, available=True)
    # cart_item_form = CartAddItemForm()
    context = {
        'item': item,
        # 'cart_item_form': cart_item_form
    }
    return render(request, 'item/item.html', context)
