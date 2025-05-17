from django.test import TestCase # type: ignore
from django.contrib.auth import get_user_model # type: ignore
from .models import Publicacion

# Create your tests here.
class PruebasBlog(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username = 'usuarioprueba',
            email = 'prueba@email.com',
            password = "secreto"
        )
        cls.publicacion = Publicacion.objects.create(
            titulo = 'Un buen título',
            contenido = 'Muy buen contenido',
            autor = cls.user
        )
        
    def test_modelo_publicacion(self):
        self.assertEqual(self.publicacion.titulo, 'Un buen título')
        self.assertEqual(self.publicacion.contenido, 'Muy buen contenido')
        self.assertEqual(self.publicacion.autor.username, 'usuarioprueba')
        self.assertEqual(str(self.publicacion), 'Un buen título')
        self.assertEqual(self.publicacion.get_absolute_url(), '/pub/1/')

