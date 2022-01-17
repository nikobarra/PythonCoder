from django.contrib import admin
from .models import CatProducto, Product

# Register your models here.

class CatProductoAdmin(admin.ModelAdmin):
    readonly_fields =("created", "updated")
    
class ProductAdmin(admin.ModelAdmin):
    readonly_fields =("created", "updated")
    
admin.site.register(CatProducto, CatProductoAdmin)
admin.site.register(Product, ProductAdmin)
