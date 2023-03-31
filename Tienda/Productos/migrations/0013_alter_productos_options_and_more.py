# Generated by Django 4.1.5 on 2023-03-31 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0012_alter_productos_options_productos_fechapublicacion'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productos',
            options={'ordering': ['usuario']},
        ),
        migrations.RemoveField(
            model_name='productos',
            name='fechaPublicacion',
        ),
        migrations.AlterField(
            model_name='productos',
            name='imagenProducto',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes/'),
        ),
        migrations.AlterField(
            model_name='productos',
            name='producto',
            field=models.CharField(choices=[('guitarra', 'Guitarra'), ('bajo', 'Bajo'), ('pedal', 'Pedal'), ('bateria', 'Bateria'), ('teclado', 'Teclado'), ('amplificador', 'Amplificador'), ('otro', 'Otro')], default='computadora', max_length=15),
        ),
    ]
