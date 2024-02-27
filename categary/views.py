from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import categary, products, cart, billing, order
from .serializers import CategarySerializer, ProductReadSerializer, ProductWriteSerializer, CartReadSerializer, CartWriteSerializer, BillingReadSerializer, \
    BillingWriteSerializer, OrderReadSerializer, OrderWriteSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status



class CategaryViewSet(viewsets.ModelViewSet):
    queryset = categary.objects.all()
    serializer_class = CategarySerializer
    permission_classes = [permissions.IsAuthenticated]  # Example: Use IsAuthenticated, you can customize based on your needs


class ProductViewSet(viewsets.ModelViewSet):
    queryset = products.objects.all()
    #serializer_class =  ProductSerializer   
    def get_serializer_class(self):
        if self.action in ('create', 'update', 'partial_update',):
            return ProductWriteSerializer
        return ProductReadSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = products.objects.all()
        category_id = self.request.query_params.get('category_id', None)
        if category_id is not None:
            queryset = queryset.filter(category_id=category_id)
        return queryset
    
    @action(detail=True, methods=['get'])
    def products_by_category(self, request, pk=None):
        # category_id = products.objects.filter(category_id=pk)
        if pk is not None:
            #queryset = self.queryset.select_related('categary').filter(categary=pk)
            queryset = self.queryset.filter(categary=pk)
            print()
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return Response({"error": "Category ID parameter is required"}, status=status.HTTP_400_BAD_REQUEST)        

class CartViewSet(viewsets.ModelViewSet):   
    queryset = cart.objects.filter()
    def get_serializer_class(self):
        if self.action in ('create', 'update', 'partial_update',):
            return CartWriteSerializer
        return CartReadSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user 
        queryset = cart.objects.filter(user=user)
        return queryset
    
    @action(detail=True, methods=['get'])
    def carts_by_user(self, request, pk=None):
        if pk is not None:
            queryset = self.queryset.filter(user=pk)
            print()
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return Response({"error": "Category ID parameter is required"}, status=status.HTTP_400_BAD_REQUEST)


def add_categary_view(request):
    return render(request, "Add.html")
def add_product_view(request):
    return render(request, "addproduct.html")
def render_index_page(request):
    #access_token = get_access_token_from_database(request.user)
    #refresh_token = get_refresh_token_from_database(request.user)
    return render(request, "index.html")
def render_cart_view(request):
    return render(request, "cart.html")
def render_checkout_view(request):
    return render(request, "checkout.html")


class BillingViewSet(viewsets.ModelViewSet):   
    queryset = billing.objects.all()
    def get_serializer_class(self):
        if self.action in ('create', 'update', 'partial_update'):
            return BillingWriteSerializer
        return BillingReadSerializer
    permission_classes = [permissions.IsAuthenticated]

    # def get_queryset(self):
    #     user = self.request.user 
    #     queryset = billing.objects.all()
    #     return queryset

class OrderViewSet(viewsets.ModelViewSet):   
    queryset = order.objects.all()
    def get_serializer_class(self):
        if self.action in ('create', 'update', 'partial_update'):
            return OrderWriteSerializer
        return OrderReadSerializer
    permission_classes = [permissions.IsAuthenticated]