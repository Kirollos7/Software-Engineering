from django.urls import path
from . import views

urlpatterns = [
    path('', views.product, name='product'),
    
    path('product_detail/', views.product_detail,name='product_detail'),
]
