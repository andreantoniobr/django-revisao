from django.shortcuts import render
from .models import Client, Order, Product

def get_clients(request):
    clients = Client.objects.all()
    return render(request, 'clients.html', {'clients': clients})

def get_orders(request):
    orders = Order.objects.all()
    return render(request, 'orders.html', {'orders': orders})

def get_products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})
