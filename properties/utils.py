from django.core.cache import cache
from .models import Property


def get_all_properties():
    """
    Returns all Property objects.
    Uses Redis low-level caching for 1 hour.
    """
    queryset = cache.get('allproperties')

    if queryset is None:
        queryset = Property.objects.all()
        cache.set('all_properties', queryset, 3600)

    return queryset
