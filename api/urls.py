
from django.urls import path
from .views import HomeView, UpdateProduct,ShowProduct, ApiOverView, ShowAll,CreateProduct, DeleteProduct

urlpatterns = [
    
    #path('', HomeView, name="home" ),
    path('', ApiOverView, name="api" ),
    path('product-list/', ShowAll, name='products'),
    path('product-detail/<int:pk>', ShowProduct, name="product"),
    path('create/', CreateProduct, name="create"),
    path('update-product/<int:pk>', UpdateProduct, name="update-product"),
     path('delete-product/<int:pk>', DeleteProduct, name="delee-product"),
]
