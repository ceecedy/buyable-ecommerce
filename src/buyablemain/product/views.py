# django essentials
from django.shortcuts import render
# product model
from .models import Products

# View specific product 
def specific_product(request):
    # specific_product = Products.objects.get()
    
    return render(request, 'product/specific_product.html')