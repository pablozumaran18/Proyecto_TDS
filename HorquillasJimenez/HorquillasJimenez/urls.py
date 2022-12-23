"""HorquillasJimenez URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("home/", home, name="home"),
    path("maquina_list/",MaquinaListView.as_view(), name="maquina_list"),
    path("maquina_register/",MaquinaCreate.as_view(), name="maquina_register"),
    path("maquina_deleted/<str:pk>/",MaquinaDelete.as_view(), name="maquina_deleted"),
    path("maquina_edit/<str:pk>/",MaquinaUpdate.as_view(), name="maquina_edit"),
#_____________________________________________________________________________________________________________________________

    path("cliente_list/",ClienteListView.as_view(), name="cliente_list"),
    path("cliente_register/",ClienteCreate.as_view(), name="cliente_register"),
    path("cliente_deleted/<str:pk>/",ClienteDelete.as_view(), name="cliente_deleted"),
    path("cliente_edit/<str:pk>/",ClienteUpdate.as_view(), name="cliente_edit"),


    path('',inicio_sesion,name="inicio_sesion"),
    path("sesion_iniciada/", login_inicio, name="sesion_iniciada"),


]