# Generated by Django 4.1.5 on 2023-03-12 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sucursales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=40)),
                ('disponibilidad', models.CharField(max_length=20)),
                ('estacionamiento', models.BooleanField()),
            ],
        ),
    ]
