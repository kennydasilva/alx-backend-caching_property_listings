from django.shortcuts import render
from django.views.decorators.cache import cache_page
from .models import Property


#cache
@cache_page(60*15)
def property_list(request):
    """ the View that returns all properties.
    the response is stored in the cache on redis for 15 minutes."""

    properties= Property.objects.all()
    return render(request, "properties/property_list.html", {"properties": properties})
