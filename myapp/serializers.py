from rest_framework import serializers
from .models import Product
from .models import General
from .models import Time

class Product_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'name', 'price'
        )

class General_Serializer(serializers.ModelSerializer):
    class Meta:
        model = General
        fields = (
            'deadline', 'requiredtime'
        )

class Time_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Time
        fields = (
            'acountName', 'acountNumber', 'day', 'timearray', 'key'
        )