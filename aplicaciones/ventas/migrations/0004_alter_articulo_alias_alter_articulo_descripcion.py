# Generated by Django 4.1 on 2022-09-09 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0003_articulo_factura_alter_cliente_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='alias',
            field=models.CharField(max_length=100, unique=True, verbose_name='Alias'),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='descripcion',
            field=models.CharField(max_length=100, unique=True, verbose_name='Descripcion'),
        ),
    ]
