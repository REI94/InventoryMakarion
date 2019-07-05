# Generated by Django 2.2.2 on 2019-07-04 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('tipo_documento_id', models.CharField(choices=[('V', 'Venezolano'), ('E', 'Extranjero'), ('P', 'P - RIF'), ('J', 'J- RIF'), ('G', 'G - RIF'), ('R', 'R - Firma personal')], max_length=1, verbose_name='Tipo documento de identidad')),
                ('documento_id', models.CharField(max_length=12, primary_key=True, serialize=False, verbose_name='Documento de identidad')),
                ('telefono', models.CharField(max_length=15, verbose_name='Teléfono')),
                ('edad', models.IntegerField(verbose_name='Edad')),
                ('direccion', models.CharField(max_length=50, verbose_name='Dirección')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
