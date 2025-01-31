from django.urls import path
from .views import ProductListCreate, ProductRetrieveUpdateDestroy

urlpatterns = [
    path('', ProductListCreate.as_view(), name='product_list_create'),
    path('<int:pk>', ProductRetrieveUpdateDestroy.as_view(), name='product_detail_update_delete')
]