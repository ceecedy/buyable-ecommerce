from django.db import models

# Create your models here.

# Categories Model
class Category(models.Model):
    # declarations
    name = models.CharField(max_length=255, blank=False, null=False)
    slugname = models.SlugField()
    
    class Meta: 
        ordering = ('name', ) 
    
    # custom return 
    def __str__(self):
        return self.name
    
# Product Model
class Products(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=False, null=False)
    slugname = models.SlugField()
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True) 
    
    class Meta: 
        ordering = ('-created_at', ) # to sort the products in descending order.
        verbose_name_plural = 'Products' 
        
    def __str__(self):
        return self.name

    # function to show the price of the item 
    def get_price(self):
        return self.price 
        