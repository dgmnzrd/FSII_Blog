from django.urls import path # type: ignore
from .views import VistaRegistro

urlpatterns = [
    path('registro/', VistaRegistro.as_view(), name = 'registro'),
]
