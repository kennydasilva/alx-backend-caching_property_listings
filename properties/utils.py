from django.core.cache import cache
from .models import Property


def getallproperties():
    """
    Returns all Property objects.
    Uses Redis low-level caching for 1 hour.
    """
    queryset = cache.get('allproperties')

    if queryset is None:
        queryset = Property.objects.all()
        cache.set('allproperties', queryset, 3600)

    return queryset
