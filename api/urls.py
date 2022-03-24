from django.urls import path
from api.src.product import ProductView

urlpatterns = [
    path('getProducts', ProductView.getProduct, name='getProducts'),
    path('getProductById', ProductView.getProductById, name='getProductById'),
    path('createProduct', ProductView.createProduct, name='createProduct')
]