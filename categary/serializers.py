from rest_framework import serializers
from .models import categary, products, cart, billing, order
from aut.serializers import UserSerializer

class CategarySerializer(serializers.ModelSerializer):
    class Meta:
        model = categary
        fields = ('id','title', 'description')


class ProductReadSerializer(serializers.ModelSerializer):
    categary = CategarySerializer()  # Nested Serializer
    #cart_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True) 
    cart_set= serializers.SerializerMethodField()


    class Meta:
        model = products
        fields = ('id','title', 'price', 'quantity', 'image', 'description', 'categary','cart_set')
  
    def get_cart_set(self,obj):
        cart_products = obj.cart_set.all()
        user = self.context['request'].user.id
        cart_data = []
        for cart_product in cart_products:
            if cart_product.user.id == user:
                cart_data.append({
                    'id': cart_product.id,
                    'product_id': cart_product.product.id,
                    'user_id': cart_product.user.id
                })
        return cart_data

class ProductWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = products
        fields = ('id','title', 'price', 'quantity', 'image', 'description', 'categary')


class CartReadSerializer(serializers.ModelSerializer):
    product = ProductReadSerializer()  # Nested Serializer
    user = UserSerializer()
    class Meta:
        model = cart
        fields = ('id','quantity','product','user')

class CartWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = cart
        fields = ('quantity','product','user')


class BillingReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = billing
        fields = ('id','first_name','last_name','company_name','address','city','country','post_code','notes')

class BillingWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = billing
        fields = ('id','first_name','last_name','company_name','address','city','country','post_code','notes')


class OrderReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = order
        fields = ('id','user','billing','price','product','quantity','date')

class OrderWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = order
        fields = ('id','user','billing','price','product','quantity','date')        
