from django.db import models
from core.base_models import BaseModel
from core.managers import ClientManager, OrderManager

class Client(BaseModel):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    birth_date = models.DateField()

    objects = ClientManager()

    def delete(self):
        self.is_deleted=True
        self.save()

    def restore(self):
        self.is_deleted=False
        self.save()

    def __str__(self):
        return self.name
    

class Order(BaseModel):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('cancelled', 'Cancelled'),
    ]

    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name='orders'
    )
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    objects = OrderManager()

    def __str__(self):
        return f"Order #{self.id} - {self.client.name} - {self.status}"
