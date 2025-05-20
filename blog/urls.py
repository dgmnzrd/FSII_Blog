from django.urls import path # type: ignore
from .views import VistaListaBlog, VistaDetallePublicacion, VistaCrearPublicacion, VistaEditarPublicacion, VistaEliminarPublicacion # lista_publicacion, detalle_publicacion

urlpatterns = [
    path('', VistaListaBlog.as_view(), name = 'inicio'),
    path('pub/<int:pk>/', VistaDetallePublicacion.as_view(), name = 'detalle_publicacion'),
    path('pub/nueva/', VistaCrearPublicacion.as_view(), name = 'nueva_publicacion'),
    path('pub/<int:pk>/editar/', VistaEditarPublicacion.as_view(), name = 'editar_publicacion'),
    path('pub/<int:pk>/eliminar/', VistaEliminarPublicacion.as_view(), name = 'eliminar_publicacion')
]

# urlpatterns = [
#     path('', lista_publicacion, name='inicio'),
#     path('pub/<int:pk>/', detalle_publicacion, name='detalle_publicacion'),
# ]