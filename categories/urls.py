from django.urls import path
from .views import CategoryListCreate, CategoryRetrieveUpdateDestroy

urlpatterns = [
    path('', CategoryListCreate.as_view(), name='category_list_create'),
    path('<int:pk>/', CategoryRetrieveUpdateDestroy.as_view(), name='category_detail_update_delete'),

]