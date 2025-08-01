from django.db import models
#from proveedores.models import Proveedor
# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    proveedor = models.ForeignKey('Proveedor.Proveedor', on_delete=models.CASCADE, related_name='productos')

    def __str__(self):
        return self.nombre