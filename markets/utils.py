from markets.models import MarketItemPrice, MarketItem
from rest_framework.response import Response

def get_market_item_current_price(market, market_item_id):
    try:
        price = MarketItemPrice.objects.filter(
            market_item=market_item_id,
            ).order_by("-created_at").first().price
    except AttributeError:
        price = None
    return price


def get_market_item_or_none(pk, market_item_id):
    try:
        return MarketItem.objects.get(id=market_item_id, market=pk)
    except MarketItem.DoesNotExist:
        return None