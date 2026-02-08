from rest_framework import serializers
from .models import Product

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields="__all__"
        
    def get_image(self, obj):
        if obj.image:
            return f"https://djangoclickmart.online{obj.image.url}"
        return None
    