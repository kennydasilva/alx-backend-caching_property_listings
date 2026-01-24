from django.core.cache import cache
from .models import  Property


def get_all_properties():
    """
    Returns all properties using a low level cache
    -if exist cache on redis ,returns cache.
    - if not exists , query the databbase and store the cache for 1h
    """

    #check the cache 
    properties =cache.get(all_properties)
    if properties is not None:
        return properties
    

    