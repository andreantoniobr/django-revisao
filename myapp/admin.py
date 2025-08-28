from django.contrib import admin

# Register your models here.
from .models import Order, Client, Product

admin.site.register(Client)
admin.site.register(Order)
admin.site.register(Product)
