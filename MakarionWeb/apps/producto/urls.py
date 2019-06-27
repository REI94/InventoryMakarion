from django.urls import path
from .views import Indexproducto, crearProducto, BolsosListView
from .views import CarterasListView, CartucherasListView, VerProducto

urlpatterns = [
    path('', Indexproducto, name = 'producto'),
    path('ingresar_producto', crearProducto, name = 'ingresar_producto'),
    path('bolsos', BolsosListView.as_view(), name = 'producto_bolso'), 
    path('carteras', CarterasListView.as_view(), name = 'producto_carteras'),
    path('cartucheras', CartucherasListView.as_view(), name = 'producto_cartucheras'),
    path('verProducto', VerProducto.as_view(), name = 'ver_producto'),  
]

