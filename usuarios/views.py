from django.views.generic import CreateView # type: ignore
from django.contrib.auth.forms import UserCreationForm # type: ignore
from django.urls import reverse_lazy # type: ignore

# Create your views here.
class Registro(CreateView):
    form_class = UserCreationForm
    template_name = 'registro.html'
    success_url = reverse_lazy('registration/signup.html')
