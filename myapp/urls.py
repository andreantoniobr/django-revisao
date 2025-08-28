from django.urls import path
from .views import get_clients, get_orders, get_products

urlpatterns = [
    path('clients/', get_clients, name='get_clients'),
    path('products/', get_products, name='get_products'),
    path('orders/', get_orders, name='get_orders'),
]
