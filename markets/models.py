from django.db import models
from products.models import Product


class Market(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class MarketItem(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.PROTECT)
    market = models.ForeignKey(to=Market, on_delete=models.PROTECT, related_name='products')
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product} - {self.market}"


class MarketItemPrice(models.Model):
    market_item = models.ForeignKey(to=MarketItem, on_delete=models.PROTECT, related_name='prices')
    price = models.DecimalField(decimal_places=2, max_digits=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.market_item} - {self.price} - {self.created_at}"
    