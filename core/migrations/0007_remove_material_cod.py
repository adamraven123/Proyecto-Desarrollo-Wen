# Generated by Django 2.0.6 on 2018-06-26 22:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_remove_cliente_rut'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='material',
            name='cod',
        ),
    ]