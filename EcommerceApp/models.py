from django.db import models

# Create your models here.
class CatProducto (models.Model):
    nombre=models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name="CatPro"
        verbose_name_plural="CatProds"
        
    def __str__(self):
        return self.nombre
    
class Product(models.Model):
    nombre = models.CharField(max_length=30)
    categoria = models.ForeignKey(CatProducto, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="ecommerce_img", null=True, blank=True)
    stock= models.BooleanField(default=True)
    precio= models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        
    def __str__(self):
        return self.nombre
    
    