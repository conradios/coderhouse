# Generated by Django 4.1.5 on 2023-03-29 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0005_alter_productos_imagenproducto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='imagenProducto',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes/'),
        ),
    ]
