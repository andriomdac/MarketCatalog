from django.db import models
from brands.models import Brand
from categories.models import Category


class Product(models.Model):
    name = models.CharField(max_length=255)
    brand = models.ForeignKey(to=Brand, on_delete=models.PROTECT, related_name='products', default=None)
    category = models.ForeignKey(to=Category, on_delete=models.PROTECT, related_name='products', default=None)
    barcode = models.CharField(max_length=100, unique=True, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name