from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import response
from django.views.decorators.csrf import csrf_exempt
from products.models import Product
from products.serializers import ProductSerializer
#

class ProductViewSet(viewsets.ViewSet):

    def list(self,request):

        products=Product.objects.all()
        serializer=ProductSerializer(products,many=True)
        return response(serializer.data)

    @csrf_exempt
    def create(self,request):
        serializer=ProductSerializer(data=request.POST)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)

    def retrieve(self,request,pk=None):
        pass

    def update(self,request,pk=None):
        pass

    def destroy(self,request,pk=None):
        pass



