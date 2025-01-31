from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/token/', include('authentication.urls')),

    path('api/v1/brands/', include('brands.urls')),
    path('api/v1/categories/', include('categories.urls')),
    path('api/v1/markets/', include('markets.urls')),
    path('api/v1/products/', include('products.urls')),
]
