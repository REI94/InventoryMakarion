from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import CreateView
from apps.producto.models import Producto

from .forms import CustomUserCreationForm


# Create your views here.

def index(request):
    producto = Producto.objects.all()
    producto = Producto.objects.filter(categoria__icontains='bolso')
    print(producto)

    producto1 = Producto.objects.filter(categoria__icontains='cartera')
    #print(producto1)

    producto2 = Producto.objects.filter(categoria__icontains='cartuchera')
    return render(request, 'index.html', {'producto':producto, 'producto1':producto1, 'producto2':producto2},)

    #cliente/index.html es el template

class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('index')
    template_name = 'signup.html'
