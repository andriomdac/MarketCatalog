from django.http import JsonResponse
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class ProductListCreate(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



