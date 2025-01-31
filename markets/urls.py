from django.urls import path
from .views import (
    MarketListCreate, MarketRetrieveUpdateDestroy,
    MarketItemListCreate, MarketItemDetailDelete,
    MarketItemPriceView,
    )

urlpatterns = [
    path(
        '',
        MarketListCreate.as_view(),
        name='market_list_create'
        ),
    path(
        '<int:pk>/',
        MarketRetrieveUpdateDestroy.as_view(),
        name='market_detail_update_delete'
        ),
    path(
        '<int:pk>/products/',
        MarketItemListCreate.as_view(),
        name='market_item_list_create'
        ),
    path(
        '<int:pk>/products/<int:market_item_id>/',
        MarketItemDetailDelete.as_view(),
        name='market_item_detail_delete'
        ),
    path(
        '<int:pk>/products/<int:market_item_id>/prices/',
        MarketItemPriceView.as_view(),
        name='market_item_price'
        )
]