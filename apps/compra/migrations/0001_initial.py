# Generated by Django 2.2.2 on 2019-07-15 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('idCompra', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('MontoTotal', models.DecimalField(decimal_places=2, max_digits=18)),
            ],
        ),
    ]
