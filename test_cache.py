#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alx_backend_caching_property_listings.settings')
django.setup()

from django.core.cache import cache
from properties.models import Property

# Limpar cache anterior
cache.clear()
print("✓ Cache limpo")

# Criar algumas propriedades de teste
properties_data = [
    {"title": "Apartamento em São Paulo", "description": "Lindo apartamento", "price": 5000.00, "location": "São Paulo"},
    {"title": "Casa em Rio de Janeiro", "description": "Casa espaçosa", "price": 8000.00, "location": "Rio de Janeiro"},
    {"title": "Flat em Brasília", "description": "Flat moderno", "price": 3000.00, "location": "Brasília"},
]

# Deletar propriedades antigas
Property.objects.all().delete()
print("✓ Propriedades antigas deletadas")

# Criar novas propriedades
for data in properties_data:
    Property.objects.create(**data)
print(f"✓ {Property.objects.count()} propriedades criadas")

# Chamar a função que popula o cache
from properties.utils import getallproperties
properties = getallproperties()
print(f"✓ getallproperties() chamado - {len(properties)} propriedades em cache")

# Verificar se está no Redis
cached_properties = cache.get('allproperties')
print(f"✓ Cache 'allproperties': {cached_properties}")

print("\nVerifique o Redis agora:")
print("docker exec -it redis_cache redis-cli")
print("SELECT 1")
print("KEYS *")
