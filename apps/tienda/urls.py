from django.urls import path
from .views import registrarCliente
#from .views import home

urlpatterns = [
    #path('', home, name = 'index'),
    path('registro/', registrarCliente, name = 'registro')
]