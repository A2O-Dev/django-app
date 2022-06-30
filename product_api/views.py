from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Product
from .serializers import ProductSerializer


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'products': reverse(ProductListView.name, request=request)
        })


class ProductListView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    name = 'product-list'


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    name = 'product-detail'
