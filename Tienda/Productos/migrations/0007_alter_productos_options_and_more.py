# Generated by Django 4.1.5 on 2023-03-29 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0006_alter_productos_imagenproducto'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productos',
            options={},
        ),
        migrations.AlterField(
            model_name='productos',
            name='imagenProducto',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes'),
        ),
    ]
