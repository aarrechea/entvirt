""" Imports """
from django.db import models
from django.conf import settings



""" Owner abstract class """
class OwnerModel(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    class Meta:
        abstract=True



""" Categoria """
class Categoria(OwnerModel):
    descripcion = models.CharField(max_length=100, help_text="Descripción de la categoría")
    unique = True
    
    
    def __str__(self):
        return '{}'.format(self.descripcion)
    
    class Meta:
        verbose_name_plural = "Categorías"
        
        
""" Subcategoría """
class Subcategoria(OwnerModel):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=100, help_text="Descripción de la subcategoría")
    
    def __str__(self):
        return '{}'.format(self.categoria.descripcion, self.descripcion)
    
    class Meta:
        verbose_name_plural = "Subcategorías"
        unique_together = ('categoria', 'descripcion')
        

""" Producto """
class Producto(OwnerModel):
    subcategoria = models.ForeignKey(Subcategoria, on_delete=models.CASCADE)
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción del Producto',
        unique=True
    )
    fecha_creado = models.DateTimeField()
    vendido = models.BooleanField(default=False)
 
    def __str__(self):
        return '{}'.format(self.descripcion)
 
    class Meta:
        verbose_name_plural = "Productos"        
        
        
    



