from django.urls import path
from .views import index, SignUp

urlpatterns = [
    #path('crear_cliente/',crearCliente, name = 'crear_cliente'),
    ###path('', index, name='index'),
    path('signup/', SignUp.as_view(), name='signup'),
    #path('registrar', RegistroUsuario.as_view(), name = 'registrar'),
]