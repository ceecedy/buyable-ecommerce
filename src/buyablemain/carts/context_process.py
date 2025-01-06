# import class Cart 
from .cart import Cart

# cart view 
def cart(request):
    return {
        'cart': Cart(request)
    }