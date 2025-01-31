from django.urls import path
from .views import BrandListCreate, BrandRetrieveUpdateDestroy

urlpatterns = [
    path('', BrandListCreate.as_view(), name='brand_list_create'),
    path('<int:pk>/', BrandRetrieveUpdateDestroy.as_view(), name='brand_detail_update_delete'),

]