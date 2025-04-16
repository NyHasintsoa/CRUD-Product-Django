from django.test import TestCase
from django.core.paginator import Paginator
from .models import Product

# Create your tests here.

products = Product.objects.all()
pagination = Paginator(object_list=products, per_page=5)

# pagination.count => Compte le nombre de produit

# pagination.num_pages => Compte le nombre de page utile

# pagination.page(1) => la page où l'on veut aller

# print(type(pagination.page_range))

page1 = pagination.page(1)
print(page1.object_list)