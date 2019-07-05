from django.urls import path
from .views import crearCliente, index, RegistroUsuario

"""from .views import RegistrarUsuario"""

urlpatterns = [
    #path('crear_cliente/',crearCliente, name = 'crear_cliente'),
    path('', index, name='index'),
    #path('registrar', RegistroUsuario.as_view(), name = 'registrar'),
    path('registro/', RegistroUsuario.as_view(), name = 'registro')
]



