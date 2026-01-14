from rest_framework import serializers
from .models import Cart, CartItem


class CartItemSerializer(serializers.ModelSerializer):
    product_name=serializers.CharField(source='product.name', read_only=True)
    price=serializers.CharField(source='product.price', read_only=True)
    tax_percent=serializers.CharField(source='product.tax_percent', read_only=True)
    class Meta:
        model=CartItem
        fields= "__all__"



class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)
    subtotal = serializers.DecimalField(max_digits=10, decimal_places=2)
    grand_total = serializers.DecimalField(max_digits=10, decimal_places=2)
    class Meta:
        model = Cart
        fields = "__all__"
        
    # def get_subtotal(self, obj): # obj means cart model instance  
    #     subtotal = 0  
    #     for item in obj.items.all():
    #         subtotal+= item.product.price * item.quantity  
    #     return subtotal 
    
    # def get_total(self,obj):
    #     total= 0 
    #     for item in obj.items.all():
    #         subtotal = item.product.price * item.quantity
    #         tax = subtotal * (item.product.tax_percent / 100)
    #         total += subtotal + tax
    #     return total  
            
        
