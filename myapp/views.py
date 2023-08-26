from django.views.generic import View
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import Product_Serializer
from .serializers import General_Serializer
from .serializers import Time_Serializer
from .models import Product
from .models import General
from .models import Time

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "myapp/index.html")

class ProductView(APIView):
    permission_classes = (IsAuthenticated, )
    def get(self, request, *args, **kwargs):
        qs = Product.objects.all()
        serializer = Product_Serializer(qs, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = Product_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class GeneralView(APIView):
    def get(self, request, *args, **kwargs):
        qs = General.objects.all()
        serializer = General_Serializer(qs, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = General_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
class TimeView(APIView):
    def get(self, request, *args, **kwargs):
        qs = Time.objects.all()
        serializer = Time_Serializer(qs, many=True)
        return Response(serializer.data)
    def post(self, request, *args, **kwargs):
        serializer = Time_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)