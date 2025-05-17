from django.db import models # type: ignore
from django.urls import reverse # type: ignore

# Create your models here.
class Publicacion(models.Model):
    titulo = models.CharField(max_length = 200)
    autor = models.ForeignKey('auth.User',on_delete = models.CASCADE)
    contenido = models.TextField()

    def __str__(self):
        return self.titulo
    
    def get_absolute_url(self):
        return reverse('detalle_publicacion', kwargs = {'pk': self.pk})