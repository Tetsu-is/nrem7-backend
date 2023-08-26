from rest_framework import serializers
from .models import Product


class Product_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'name', 'price'
        )