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
        'Detail View' : '/product_detail/<int:id>',
        'create' : '/product-create/'
    }
    return Response(api_urls)
    
@api_view(['GET'])
def ShowAll(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)
