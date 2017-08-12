from django.shortcuts import get_object_or_404, render
from .models import *
from .forms import *


def home(request):
    """This is the view for the home page

    Note:
        The context in home needs to be made global
    """
    context = {
        'categories': Category.objects.all(),
        'items': Item.objects.filter(visible=True)
    }
    template = 'home.html'
    return render(request, template, context)

def about(request):
    """This is the view for the homepage

    Note:
        Page is static
    """
    context = {}
    template = 'about.html'
    return render(request, template, context)

def item_list(request, category_slug=None):
    """This is the view for a search quary


    """
    category = None
    categories = Category.objects.all()
    items = Item.objects.filter(visible=True)
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
    """This is the view for a item Page
    """
    item = get_object_or_404(Item, id=id, visible=True)
    # cart_item_form = CartAddItemForm()
    context = {
        'item': item,
        'listing': Listing.objects.filter(item=item, visible=True)
        # 'cart_item_form': cart_item_form
    }
    template = 'item/item.html'
    return render(request, template, context)

def listing(request, id, item_slug, item_id):
    """This is the view for a listing page
    """
    listing = get_object_or_404(Listing, id=id, visible=True)
    item = listing.item
    context = {
        'listing': listing,
        'item': item
    }
    template = 'item/listing.html'
    return render(request, template, context)

def post_listing(request):
    """This is the view for the sell page

    Return:
        If the form is valid it redirects home else it returns the page again.
    """
    if request.method == 'POST':
        form = PostListingForm(request.POST)
        if form.is_valid():
            listing = Listing.objects.get(id=id)
            return redirect(home)
    else:
        form = PostListingForm()
    return render(request, 'sell.html', {'form': form})
