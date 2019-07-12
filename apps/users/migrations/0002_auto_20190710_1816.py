# Generated by Django 2.2.2 on 2019-07-10 22:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='completeuser',
            name='cedula',
            field=models.CharField(help_text='Ejemplo: V011223318', max_length=10, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator(message='Cédula ingresada incorrectamente, debe ingresarla nuevamente.', regex='^[V|E]{1}[0]{1}[0-9]{7,9}$')], verbose_name='Cédula'),
        ),
        migrations.AlterField(
            model_name='completeuser',
            name='direccion',
            field=models.TextField(verbose_name='Dirección'),
        ),
        migrations.AlterField(
            model_name='completeuser',
            name='telefono',
            field=models.CharField(max_length=12, verbose_name='Teléfono'),
        ),
    ]
