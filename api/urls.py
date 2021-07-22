
from django.urls import path
from .views import HomeView, ApiOverView, ShowAll

urlpatterns = [
    
    #path('', HomeView, name="home" ),
    path('', ApiOverView, name="api" ),
    path('product-list/', ShowAll, name='products'),
]
