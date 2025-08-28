from django.db import models

class ClientQuerySet(models.QuerySet):
    def actives(self):
        return self.filter(is_deleted=False)


class ProductQuerySet(models.QuerySet):
    def actives(self):
        return self.filter(is_deleted=False)

class OrderQuerySet(models.QuerySet):
    def paid(self):
        return self.filter(status='paid')

    def pending(self):
        return self.filter(status='pending')

    def cancelled(self):
        return self.filter(status='cancelled')

    def recent(self):
        return self.order_by('-created_at')

