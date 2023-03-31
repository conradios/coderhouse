from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Productos(models.Model):
    Seleccion = (
    ('computadora','Computadora'),
    ('laptops', 'Laptops'),
    ('celulares','Celulares'),
    ('tablets','Tablets'),
    ('televisores','Televisores'),
    )
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    titulo = models.CharField(max_length=200, null=True)
    producto = models.CharField(max_length=15, choices=Seleccion, default='computadora')
    marca = models.CharField(max_length=40, null=True)
    modelo = models.CharField(max_length=40, null=True)
    descripcion = models.TextField(null=True, blank=True)
    year = models.IntegerField(null=True) 
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fechaPublicacion = models.DateTimeField(auto_now_add=True, null=True), 
    emailContacto = models.EmailField(null=True)
    imagenProducto = models.ImageField(null=True, blank=True, upload_to="imagenes/")

    class Meta:
        ordering = ['usuario' ]

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    comentario = models.ForeignKey(Productos, related_name='comentarios', on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=40)
    mensaje = models.TextField(null=True, blank=True)
    fechaComentario = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fechaComentario']

    def __str__(self):
        return '%s - %s' % (self.nombre, self.comentario)