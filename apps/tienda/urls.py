from django.urls import path
from .views import registro
#from .views import home

urlpatterns = [
    #path('', home, name = 'index'),
    path('registro/', registro, name = 'registro')
]