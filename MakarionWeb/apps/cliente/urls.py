from django.urls import path
from .views import crearCliente, index

"""from .views import RegistrarUsuario"""

urlpatterns = [
    path('crear_cliente/',crearCliente, name = 'crear_cliente'),
    path('', index, name='index'),
]



