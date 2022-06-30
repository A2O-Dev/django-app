import django_filters.rest_framework
from rest_framework import generics, permissions, filters
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Product
from .serializers import ProductSerializer


class ApiRoot(generics.GenericAPIView):
    name = 'Api Root'
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return Response({
            'products': reverse(ProductListView.name, request=request)
        })


class ProductListView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['name', 'code', 'price']
    ordering_fields = ['id', 'name', 'code', 'price', 'stock', 'created_at', 'updated_at']
    name = 'product-list'


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    name = 'product-detail'
