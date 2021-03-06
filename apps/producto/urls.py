from django.urls import path, re_path
from .views import Indexproducto, ProductoCreate, BolsosListView
from .views import CarterasListView, CartucherasListView, verProductoDetailView

urlpatterns = [
    path('', Indexproducto, name = 'producto'),
    path('ingresar_producto', ProductoCreate.as_view(), name = 'ingresar_producto'),
    path('bolsos', BolsosListView.as_view(), name = 'producto_bolso'), 
    path('carteras', CarterasListView.as_view(), name = 'producto_carteras'),
    path('cartucheras', CartucherasListView.as_view(), name = 'producto_cartucheras'),
    re_path('^verProducto/(?P<pk>\d+)$', verProductoDetailView.as_view(), name='producto-detail')  
]
