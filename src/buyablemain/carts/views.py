# django essentials
from django.shortcuts import render

# import cart class 
from .cart import Cart 

# cart view 
def add_to_cart(request, product_id):
    # instantiate the cart class
    cart = Cart(request)
    # add product. 
    cart.add(product_id)
    
    return render(request, 'cart/cart_list.html')