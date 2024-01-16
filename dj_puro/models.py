""" Imports """
from django.db import models



""" Categoria model """
class Categoria(models.Model):
    description = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return '{}'.format(self.description)
    
    class Meta:
        verbose_name_plural = "Categorias"


