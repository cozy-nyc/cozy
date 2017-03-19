from django.http import HttpResponse
from django.template import loader

from .models import *

def profile(request):
    template = loader.get_template('profile.html')
    context = {
        'categories': Category.objects.get(id=id),
    }
    return HttpResponse(template.render(context, request))
