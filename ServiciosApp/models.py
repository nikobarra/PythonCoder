from django.db import models

# Create your models here.

class Services (models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=200)
    image = models.ImageField(upload_to='ServiciosApp') 
    """ instalar paquete pillow """
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'
    
    def __str__(self):
        return self.title