# Generated by Django 2.0.6 on 2018-06-26 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20180626_1129'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='rut',
        ),
    ]