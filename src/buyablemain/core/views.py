# django essentials 
from django.shortcuts import render
from django.db.models import Q

# products and category imports 
from product.models import Products, Category
 
# the frontpage view
def home_frontpage(request):
    # ORM - access all the products
    all_products = Products.objects.all()
    
    return render(request, 'core/frontpage.html', {'products': all_products})
    
# the shop view 
def shopping(request):
    # ORM - access all the products and categories
    all_products = Products.objects.all()
    all_categories = Category.objects.all()
    
    # Get the category slug from the request
    active_category_slug = request.GET.get('category', '')
    
    # Filter products by the active category if it exists
    if active_category_slug:
        all_products = all_products.filter(category__slugname=active_category_slug)
    
    search_query = request.GET.get('search_query', '')
    
    # if there is any searched item 
    if search_query:
        all_products = all_products.filter(Q(name__icontains = search_query) | Q(description__icontains = search_query))
    
    context = {
        'categories': all_categories,
        'products': all_products,
        'active_category': active_category_slug,
    }
    
    return render(request, 'core/shopping.html', context)