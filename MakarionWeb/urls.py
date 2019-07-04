"""MakarionWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

#from apps.cliente.views import Home

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('cliente/', include(('apps.cliente.urls', 'cliente'))),
    #path('producto/', include(('apps.producto.urls', 'producto'))),
    #path('index/',Home, name = 'index'),
]

""" """
# Use include() to add paths from the catalog application 

urlpatterns += [
    path('cliente/', include('apps.cliente.urls')),
    path('producto/', include('apps.producto.urls')),
]

#Add URL maps to redirect the base URL to our application
from django.views.generic import RedirectView
urlpatterns += [
    path('', RedirectView.as_view(url='/cliente/', permanent=True)),
    path('', RedirectView.as_view(url='/producto/', permanent=True)),
]

# Use static() to add url mapping to serve static files during development (only)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
""" """


if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)