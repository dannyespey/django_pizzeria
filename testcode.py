import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Pizzeria.settings")

import django
django.setup()

from pizzas.models import Pizza
from pizzas.models import Topping

pizzas = Pizza.objects.all()

for pizza in pizzas:
    print(pizza.id, pizza)

toppings = Topping.objects.all()

for topping in toppings:
    print(topping)