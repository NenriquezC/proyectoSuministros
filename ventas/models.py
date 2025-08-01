from django.db import models
#from productos.models import Producto
#from usuarios.models import Usuario
# Create your models here.

class Venta(models.Model):
    producto = models.ForeignKey('productos.Producto', on_delete=models.CASCADE, related_name='ventas')
    usuario = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE, related_name='ventas')
    cantidad = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Venta de {self.cantidad} {self.producto} a {self.usuario}'