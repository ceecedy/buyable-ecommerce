# django essentials
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.contrib import messages
# product model
from .models import Products

# View specific product 
def specific_product(request, slug):
    try:
        specific_product = get_object_or_404(Products, slugname=slug)
    except Http404:
        messages.error(request, 'The item is currently not available.')
        return render(request, 'product/item_not_available.html')
    
    return render(request, 'product/specific_product.html', {'product': specific_product})
    