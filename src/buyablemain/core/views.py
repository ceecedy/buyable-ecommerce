# django essentials 
from django.shortcuts import render

# products and category imports 
from product.models import Products
 
# the frontpage view
def home_frontpage(request):
    # ORM - access all the values. 
    products = Products.objects.all()
    
    return render(request, 'core/frontpage.html', {'products':products})

# the shop view 
def shopping(request):
    # ORM - access all the values. 
    products = Products.objects.all()
    
    return render(request, 'core/shopping.html', {'products':products})