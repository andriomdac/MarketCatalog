from .models import Brand
from .serializers import BrandSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class BrandListCreate(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly,]
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class BrandRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly,]
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
