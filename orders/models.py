from django.db import models

# Create your models here.
from django.db import models


class MenuOrder(models.Model):
    customer_name = models.CharField(max_length=100)
    event_name = models.CharField(max_length=100, blank=True)
    event_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer_name


class MenuSection(models.Model):

    order = models.ForeignKey(
        MenuOrder,
        on_delete=models.CASCADE,
        related_name='sections'
    )

    category = models.CharField(max_length=100)

    items = models.TextField()

    def get_items(self):
        return [
            item.strip()
            for item in self.items.splitlines()
            if item.strip()
        ]