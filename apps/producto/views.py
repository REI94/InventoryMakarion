from django.shortcuts import render, redirect

# Create your views here.
from .forms import ProductoForm

#Para importar una vista de clase
from django.views import generic

from .models import Producto
##
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

# Create your views here.
def Indexproducto(request):
    return render(request, 'producto/producto.html')

class ProductoCreate(CreateView):
    model = Producto
    fields = '__all__'
    #success_url = reverse_lazy('index')


#def ProductoCreate(request):
#    if request.method == 'POST':
#        form = ProductoForm(request.POST)
#        if form.is_valid():
#            form.save()
#        return redirect('index')

#    else:
#        form = ProductoForm()
#    return render(request, 'producto/ingresar_producto.html', {'form':form})

class BolsosListView(generic.ListView):
    model = Producto
    context_object_name = 'bolso_list'
    template_name = 'producto/bolsos/listarBolso.html'
    queryset = Producto.objects.filter(categoria__icontains='bolso')

class CarterasListView(generic.ListView):
    model = Producto
    template_name = 'producto/carteras/listarCarteras.html'
    queryset = Producto.objects.filter(categoria__contains='cartera')

class CartucherasListView(generic.ListView):
    model = Producto
    context_object_name = 'cartucheras_list'
    template_name = 'producto/cartucheras/listarCartucheras.html'
    queryset = Producto.objects.filter(categoria__contains='cartuchera')

#class VerProducto(generic.ListView):
 #   model = Producto
  #  template_name = 'producto/verProducto.html'

class verProductoDetailView(generic.DetailView):
    model = Producto
    template_name = 'producto/verProducto.html'
 