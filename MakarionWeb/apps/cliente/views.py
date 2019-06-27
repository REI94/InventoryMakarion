from django.shortcuts import render,redirect

from .forms import ClienteForm
from apps.producto.models import Producto

"""from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views import CreateView
from django.urls import reverse_lazy"""


	


# Create your views here.

#from django.http import HttpResponse

def index(request):
    producto = Producto.objects.all()
    print(producto)
    return render(request, 'index.html', {'producto':producto})

    #cliente/index.html es el template



"""	
class RegistroUsuario(CreateView):
	model = Cliente
	template_name = "cliente/registro.html"
	form_class = UserCreationForm
	success_url = reverse_lazy('cliente:index')
"""
	
def crearCliente(request):
    if request.method == 'POST':
        cliente_form = ClienteForm(request.POST)
        if cliente_form.is_valid():
            cliente_form.save()
            return redirect('index')

        else:
            cliente_form = ClienteForm()
        return render(request, 'cliente/crear_cliente.html', {'cliente_form':cliente_form})
		