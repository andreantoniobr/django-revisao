from django.db import models
from .querysets import ClientQuerySet, OrderQuerySet, ProductQuerySet

class ClientManager(models.Manager):
    def get_queryset(self):
        return ClientQuerySet(self.model, using=self._db)
    
    def actives(self):
        return self.get_queryset().actives()
    

class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)
    
    def actives(self):
        return self.get_queryset().actives()
    

class OrderManager(models.Manager):
    def get_queryset(self):
        return OrderQuerySet(self.model, using=self._db)

    def paid(self):
        return self.get_queryset().paid()

    def pending(self):
        return self.get_queryset().pending()

    def cancelled(self):
        return self.get_queryset().cancelled()

    def recent(self):
        return self.get_queryset().recent()