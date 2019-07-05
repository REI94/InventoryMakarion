from django.shortcuts import render,redirect

from .forms import ClienteForm
from apps.producto.models import Producto

#from django.contrib.auth.models import User
#from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
#from django.urls import reverse_lazy
from django.urls import reverse_lazy



	


# Create your views here.

#from django.http import HttpResponse

def index(request):
    #producto = Producto.objects.all()
    producto = Producto.objects.filter(categoria__icontains='bolso')
    print(producto)

    producto1 = Producto.objects.filter(categoria__icontains='cartera')
    #print(producto1)

    producto2 = Producto.objects.filter(categoria__icontains='cartuchera')
    return render(request, 'index.html', {'producto':producto, 'producto1':producto1, 'producto2':producto2},)

    #cliente/index.html es el template



	
class RegistroUsuario(CreateView):
	model = User
	template_name = "cliente/form.html"
	form_class = ClienteForm
	success_url = reverse_lazy('index')

	
def crearCliente(request):
    if request.method == 'POST':
        cliente_form = ClienteForm(request.POST)
        if cliente_form.is_valid():
            cliente_form.save()
            return redirect('index')
    else:
        cliente_form = ClienteForm()
        return render(request, 'cliente/form.html', {'cliente_form':cliente_form})
		