from django.shortcuts import render, redirect
from .forms import ClienteForm

# Create your views here.
def home(request):
    return render(request, 'index.html')

#def registro(request):
#    return render(request, 'form.html')

def registrarCliente(request):
    if request.method == 'POST':
        cliente_form = ClienteForm(request.POST)
        if cliente_form.is_valid():
            cliente_form.save()
            return redirect('index')
    else:
        cliente_form = ClienteForm()
        return render(request, 'form.html', {'cliente_form':cliente_form})