from django.urls import path
from .views import get_clients, get_orders

urlpatterns = [
    path('clients/', get_clients, name='get_clients'),
    path('orders/', get_orders, name='get_orders'),
]
