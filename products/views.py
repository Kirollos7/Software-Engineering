from django.shortcuts import render

# Create your views here.

def product(request):
    return render(request, 'products/product.html',{})


def product_detail(request):
    return render(request, 'products/product-detail.html',{})