"""Proyecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from Proyecto1.views import saludo , despedida , PepsiCo , Pepsi , dameFecha, calcularEdad



#Tuplas de URLs donde nos referimos a las vistas. La de admin ya viene
urlpatterns = [
    path('admin/', admin.site.urls),
    path("saludo/", saludo),
    path("ya/", despedida),
    path("now/", dameFecha),
    path("edad/<int:edad>/<int:anio>", calcularEdad),
    path("Pepsi/", Pepsi),
    path("PepsiCo/", PepsiCo),
] 

#en el path de calcularEdad pongo esa /<int:anio> porque en el path paso un numero, pero necesito aclarar que es de tipo entero, y los paths solo reciben strings (algo asi era?)