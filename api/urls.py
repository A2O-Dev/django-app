from django.urls import path
from .views import (
    ApiRoot,
    ProductDetailView,
    ProductListView,
)

urlpatterns = [
    path('', ApiRoot.as_view()),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>', ProductDetailView.as_view(), name='product-detail')
]
