from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from .models import Property
from .utils import get_all_properties

@cache_page(60 * 15)
def property_list(request):
    """
    Returns all properties as JSON.
    Response is cached in Redis for 15 minutes.
    """
    properties = get_all_properties
    data = list(properties)
    return JsonResponse({"data": data})
