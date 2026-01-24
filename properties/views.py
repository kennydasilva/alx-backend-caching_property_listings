from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from .utils import getallproperties


@cache_page(60 * 15)
def property_list(request):
    """
    Returns all properties.
    The response is cached for 15 minutes.
    The queryset is cached for 1 hour using Redis.
    """
    properties = getallproperties()

    data = [
        {
            "id": prop.id,
            "title": prop.title,
            "price": prop.price,
            "location": prop.location,
        }
        for prop in properties
    ]

    return JsonResponse({"data": data})
