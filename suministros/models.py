from django.db import models
#from productos.models import Producto
#from proveedores.models import Proveedor

class Suministro(models.Model):
    producto = models.ForeignKey('productos.Producto', on_delete=models.CASCADE, related_name='suministros')
    proveedor = models.ForeignKey('proveedores.Proveedor', on_delete=models.CASCADE, related_name='suministros')
    cantidad = models.IntegerField()
    fecha = models.DateField()

    def __str__(self):
        return f'{self.cantidad} de {self.producto} por {self.proveedor}'
