
from django.urls import path
from .views import HomeView, UpdateProduct,ShowProduct, ApiOverView, ShowAll,CreateProduct

urlpatterns = [
    
    path('home/', HomeView, name="home" ),
    path('', ApiOverView, name="api" ),
    path('product-list/', ShowAll, name='products'),
    path('product-detail/<int:pk>', ShowProduct, name="product"),
    path('create/', CreateProduct, name="create"),
    path('update-product/<int:pk>', UpdateProduct, name="update-product"),
]
