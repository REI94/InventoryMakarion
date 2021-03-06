# Generated by Django 2.2.2 on 2019-07-15 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('producto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('idCarrito', models.AutoField(primary_key=True, serialize=False)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=18)),
                ('cantidadAgregada', models.IntegerField()),
                ('producto', models.ManyToManyField(to='producto.Producto')),
            ],
        ),
    ]
