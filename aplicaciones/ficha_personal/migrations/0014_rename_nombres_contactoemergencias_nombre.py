# Generated by Django 4.1.1 on 2022-09-21 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ficha_personal', '0013_rename_empleado_id_contactoemergencias_empleado'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactoemergencias',
            old_name='nombres',
            new_name='nombre',
        ),
    ]
