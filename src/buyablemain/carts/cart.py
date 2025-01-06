# Django essentials
from django.conf import settings

# Ensure CART_SESSION_ID is defined in settings
if not hasattr(settings, 'CART_SESSION_ID'):
    settings.CART_SESSION_ID = 'cart'

# product model import 
from product.models import Products

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        
        if cart: 
            self.cart = cart
        else:
            self.cart = self.session[settings.CART_SESSION_ID] = {}
            
    def __iter__(self):
        product_ids = self.cart.keys()
        products = Products.objects.filter(pk__in=product_ids)
        products_dict = {str(product.pk): product for product in products}
        
        for k in self.cart.keys():
            self.cart[str(k)]['product'] = products_dict[str(k)]
            
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
    
    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True # to make the save work. 
        
    def add(self, product_id, quantity=1, update_quantity=False):
        product_id = str(product_id)
        
        if product_id not in self.cart: 
            self.cart[product_id] = {'quantity': 1, 'id': product_id,}
        
        if update_quantity:
            self.cart[product_id]['quantity'] += int(quantity)
            if self.cart[product_id]['quantity'] == 0:
                self.remove(product_id)
                
        self.save()
        
    def remove(self, product_id):
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()