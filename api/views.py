from django.http import response
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializer import ProductSerializer
from .models import Product

# Create your views here.

def HomeView(request):
    return render(request, "home.html")

@api_view(['GET'])
def ApiOverView(request):
    api_urls = {
        'List' : '/product-list/',
        'Detail View' : '/product-detail/<int:id>',
        'create' : '/create/',
        'update' : '/update-product/<int:id>',
    }
    return Response(api_urls)
    
@api_view(['GET'])
def ShowAll(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ShowProduct(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def CreateProduct(request):
    
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def UpdateProduct(request,pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(instance=product, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)