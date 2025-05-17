from django.views.generic import ListView, DetailView # type: ignore
from django.views.generic.edit import CreateView, UpdateView # type: ignore
from .models import Publicacion

# Create your views here.
class VistaListaBlog(ListView):
    model = Publicacion
    template_name = 'inicio.html'
    context_object_name = 'publicaciones'

class VistaDetallePublicacion(DetailView):
    model = Publicacion
    template_name = 'detalle_publicacion.html'
    
class VistaCrearPublicacion(CreateView):
    model = Publicacion
    template_name = 'nueva_publicacion.html'
    fields = ['titulo', 'autor', 'contenido']
    
class VistaEditarPublicacion(UpdateView):
    model = Publicacion
    template_name = 'editar_publicacion.html'
    fields = ['titulo', 'autor', 'contenido']

# def lista_publicacion(request):
#     publicaciones = Publicacion.objects.all()
#     return render(request, 'inicio.html', {'publicaciones': publicaciones})

# def detalle_publicacion(request, pk):
#     publicacion = get_object_or_404(Publicacion, pk = pk)
#     return render(request, 'detalle_publicacion.html', {'publicacion': publicacion})
