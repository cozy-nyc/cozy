from django.shortcuts import get_object_or_404, render

from .models import *
from .forms import *

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

def item_detail(request, id, slug):
    item = get_object_or_404(Item, id=id, available=True)
    # cart_item_form = CartAddItemForm()
    context = {
        'item': item,
        'listing': Listing.objects.filter(item=item, available=True)
        # 'cart_item_form': cart_item_form
    }
    template = 'item/item.html'
    return render(request, template, context)

def listing(request, id, item_slug, item_id):
    listing = get_object_or_404(Listing, id=id, available=True)
    item = listing.item
    context = {
        'listing': listing,
        'item': item
    }
    template = 'item/listing.html'
    return render(request, template, context)

def post_listing(request):
    if request.method == 'POST':
        form = PostListingForm(request.POST)
        if form.is_valid():
            listing = Listing.objects.get(id=id)
            return redirect(home)
    else:
        form = PostListingForm()
    return render(request, 'sell.html', {'form': form})
