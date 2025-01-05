# django essentials 
from django.shortcuts import render

# products and category imports 
from product.models import Products
 

# Create your views here.
# testing the frontpage 
def test_frontpage(request):
    # ORM - access all the values. 
    products = Products.objects.all()[0:7]
    
    return render(request, 'core/frontpage.html', {'products':products})