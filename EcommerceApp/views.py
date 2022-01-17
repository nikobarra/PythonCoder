from django.shortcuts import render
from .models import Product


# Create your views here.

def ecommerce(request):
    productos = Product.objects.all()
    return render(request, 'EcommerceApp/ecommerce.html', {'productos':productos})