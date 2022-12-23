from django import forms
from .models import *

class MaquinaForm(forms.ModelForm):
    class Meta:
        model = Maquina
        fields = ["codigo", "modelo", "operador", "estado"]
        widgets ={

            "codigo" : forms.TextInput(attrs={"class":"form-control","placeholder":"Codigo maquina"}), 
            "modelo":forms.TextInput(attrs={"class":"form-control","placeholder":"Modelo "}),
            "operador":forms.Select(attrs={"class":"form-control","placeholder":"Operador"}),
            "estado":forms.Select(attrs={"class":"form-control","placeholder":"Estado maquina"}),
            
        }


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["rut", "nombre", "apellido", "fecha","monto"]
        widgets ={

            "rut" : forms.TextInput(attrs={"class":"form-control","placeholder":"Rut"}), 
            "nombre":forms.TextInput(attrs={"class":"form-control","placeholder":"Nombre"}),
            "apellido":forms.TextInput(attrs={"class":"form-control","placeholder":"Apellido"}),
            "fecha":forms.DateInput(attrs={'class':'form-control',"placeholder":"Fecha", 'type':'date'}),
            "monto":forms.NumberInput(attrs={"class":"form-control","placeholder":"Monto a pagar"}),
        }