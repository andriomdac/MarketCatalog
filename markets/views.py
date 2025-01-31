from rest_framework.views import APIView
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    RetrieveDestroyAPIView
    )
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import Market, MarketItem, MarketItemPrice
from products.models import Product
from .serializers import MarketSerializer
from .utils import get_market_item_current_price, get_market_item_or_none
import json
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class MarketListCreate(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    queryset = Market.objects.all()
    serializer_class = MarketSerializer


class MarketRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    queryset = Market.objects.all()
    serializer_class = MarketSerializer


class MarketItemListCreate(ListCreateAPIView):
    """
    Handles listing and creating market items for a specific market.
    """
    permission_classes = [IsAuthenticatedOrReadOnly, ]

    def get(self, request, pk):
        market_items = MarketItem.objects.filter(market=pk)
        response = {
            f"{item.id}": {
                "name": item.product.name,
                "price": get_market_item_current_price(
                    market_item_id=item.id,
                    market=pk,
                    ),
                "available": item.available
            } for item in market_items
        }
        return Response(data=response, status=status.HTTP_200_OK)

    def post(self, request, pk):
        try:
            request_data_body = request.data

            product_id = request_data_body.get("product")
            available = request_data_body.get("available", True)

            product = Product.objects.get(id=product_id)
            market = Market.objects.get(id=pk)

            if MarketItem.objects.filter(product=product, market=market).exists():
                return Response(data={
                    "error": f"This product already exists in this market."
                }, status=status.HTTP_405_METHOD_NOT_ALLOWED)



            new_market_item = MarketItem.objects.create(
                product=product,
                market=market,
                available=available
            )

            response = {
                "message": f"Product '{product}' successfully added to market '{market}'."
            }
            return Response(data=response, status=status.HTTP_201_CREATED)

        except Product.DoesNotExist:
            return Response(
                {"error": f"Product ID '{product_id}' does not exist."},
                status=status.HTTP_404_NOT_FOUND
            )

        except Market.DoesNotExist:
            return Response(
                {"error": f"Market ID '{pk}' does not exist."},
                status=status.HTTP_404_NOT_FOUND
            )

        except Exception as e:
            return Response(
                {"error": f"Unexpected error: {e}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class MarketItemDetailDelete(RetrieveDestroyAPIView):
    """
    Handles retrieving and deleting a specific market item.
    """

    permission_classes = [IsAuthenticatedOrReadOnly, ]

    def get(self, request, pk, market_item_id):
        market_item = get_market_item_or_none(market_item_id=market_item_id, pk=pk)
        if market_item is not None:
            from icecream import ic
            ic(market_item)
            response = {
                f"{market_item.pk}": {
                    "name": market_item.product.name,
                    "price": get_market_item_current_price(
                        market_item_id=market_item_id,
                        market=pk
                        ),
                    "available": market_item.available
                }
            }
        else:
            response = {}
        return Response(data=response, status=status.HTTP_200_OK)

    def delete(self, request, pk, market_item_id):
        market_item = get_market_item_or_none(market_item_id=market_item_id)
        if market_item is not None:
            market_item.delete()
            response = {
                "message": f"Product '{market_item.product}' successfully deleted"
            }
        else:
            response = {}
        return Response(data=response, status=status.HTTP_204_NO_CONTENT)


class MarketItemPriceView(MarketItemDetailDelete):
    """
    GET product price history, or POST a new price to requested product
    """

    permission_classes = [IsAuthenticatedOrReadOnly, ]

    def get(self, request, pk, market_item_id):
        prices = MarketItemPrice.objects.filter(market_item=market_item_id, market_item__market=pk)
        response = {}
        if prices:
            for price in prices:
                response[f"{price.price}"] = price.created_at
        else:
            response = {"message": "No prices history found"}
        return Response(data=response, status=status.HTTP_200_OK)


    def post(self, request, pk, market_item_id):
        market_item = MarketItem.objects.get(id=market_item_id)
        request_body_data = json.loads(request.body.decode("utf-8"))
        new_price = MarketItemPrice.objects.create(
            market_item=market_item,
            price=request_body_data['price']
        )
        response = {
            "message": f"Price '{new_price.price}' successfully assigned to {market_item}"
        }
        return Response(data=response)