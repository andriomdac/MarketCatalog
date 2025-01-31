from django.contrib import admin
from .models import Market, MarketItem, MarketItemPrice


@admin.register(Market)
class MarketAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'name',
        'description',
        'created_at',
        'updated_at'
        ]
    search_fields = [
        'name',
        'description',
    ]



@admin.register(MarketItem)
class MarketItemAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'market',
        'product',
        'created_at',
        'updated_at'
        ]

@admin.register(MarketItemPrice)
class MarketItemPriceAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'market_item',
        'price',
        'created_at',
        'updated_at',
        ]
    search_fields = [
        'market_item',
        'price',
    ]