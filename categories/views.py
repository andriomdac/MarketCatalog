from .models import Category
from .serializers import CategorySerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class CategoryListCreate(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer