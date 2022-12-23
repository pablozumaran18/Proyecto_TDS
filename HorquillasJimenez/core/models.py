from django.db import models

import uuid

class Operador (models.Model):  
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    rut = models.CharField(max_length=10)
    nombre = models.CharField (max_length=30)
    apellido = models.CharField (max_length=30)

    def __str__(self):
        return self.nombre



class Estado (models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    nombre = models.CharField(max_length=20, verbose_name="Nombre Estado")

    def __str__(self):
        return self.nombre




class Maquina(models.Model):
    # id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    codigo = models.CharField(max_length=10, primary_key=True, verbose_name='codigo maquina')
    modelo = models.CharField(max_length = 20,verbose_name="modelo Maquina")
    operador = models.ForeignKey(Operador,on_delete=models.CASCADE,null=True,blank=True, verbose_name="Operador de maquina")
    estado = models.ForeignKey(Estado,on_delete=models.CASCADE,null=True,blank=True, verbose_name="Estado de maquina")

    def __str__(self):
        return self.modelo


class Cliente(models.Model):
    rut = models.CharField(max_length = 10, primary_key=True)
    nombre = models.CharField(max_length = 100)
    apellido = models.CharField(max_length = 100)
    fecha = models.DateField()
    monto= models.PositiveBigIntegerField()

    def __str__(self):
        return self.nombre



class Inicio(models.Model):
    rut = models.CharField(max_length=10)
    clave = models.CharField (max_length=8)

    def __str__(self):
        return self.rut