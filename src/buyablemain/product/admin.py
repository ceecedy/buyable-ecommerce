from django.contrib import admin

from .models import *

# registering the category model from product app in the admin view. 
admin.site.register(Category)
# registering the product model from product app in the admin view. 
admin.site.register(Products)