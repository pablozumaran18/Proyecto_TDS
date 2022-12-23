from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import *
from .forms import *
from django.urls import reverse_lazy

def login_inicio (request):
    rut = request.POST['rut']
    clave = request.POST['clave']

    lista = Inicio.objects.all()

    for a in lista:
        if rut == a.rut:
            if clave == a.clave:
                context={'context': 'Sesion iniciada correctamente'}
                return render(request, 'core/home.html', context)
            context={'context': 'La contraseña es incorrecta'}
            return render(request, 'core/inicio_sesion.html', context)
        context={'context': 'El rut ingresado no se encuentra registrado'}
        return render(request, 'core/inicio_sesion.html', context)

def inicio_sesion (request):

    return render(request,'core/inicio_sesion.html')



def home (request):
    return render(request,"core/home.html")


class MaquinaListView(ListView):
    model = Maquina


class MaquinaCreate(CreateView):
    model = Maquina
    form_class = MaquinaForm
    success_url = reverse_lazy("maquina_list") 

class MaquinaUpdate(UpdateView):
    model = Maquina
    form_class = MaquinaForm
    template_name_suffix = "_update_form"
    

    def get_success_url(self):
        return reverse_lazy("maquina_edit", args =[self.object.codigo])+"?ok" 


class MaquinaDelete(DeleteView):
    model = Maquina
    
    success_url = reverse_lazy("maquina_list") 


#___________________________________________________________________________________________________

class ClienteListView(ListView):
    model = Cliente


class ClienteCreate(CreateView):
    model = Cliente
    form_class = ClienteForm
    success_url = reverse_lazy("cliente_list") 

class ClienteUpdate(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name_suffix = "_update_form"
    

    def get_success_url(self):
        return reverse_lazy("cliente_edit", args =[self.object.rut])+"?ok" 


class ClienteDelete(DeleteView):
    model = Cliente
    
    success_url = reverse_lazy("cliente_list")