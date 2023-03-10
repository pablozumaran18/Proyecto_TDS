# Generated by Django 4.1.1 on 2022-12-20 01:19

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('rut', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('fecha', models.DateField()),
                ('monto', models.PositiveBigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20, verbose_name='Nombre Estado')),
            ],
        ),
        migrations.CreateModel(
            name='inicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=10)),
                ('clave', models.CharField(max_length=8)),
                ('rol', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Operador',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('rut', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Maquina',
            fields=[
                ('codigo', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='codigo maquina')),
                ('modelo', models.CharField(max_length=20, verbose_name='modelo Maquina')),
                ('estado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.estado', verbose_name='Estado de maquina')),
                ('operador', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.operador', verbose_name='Operador de maquina')),
            ],
        ),
    ]
