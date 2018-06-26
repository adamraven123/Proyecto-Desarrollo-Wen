# Generated by Django 2.0.6 on 2018-06-26 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_capapastel_pastel'),
    ]

    operations = [
        migrations.AddField(
            model_name='pastel',
            name='cover',
            field=models.CharField(choices=[('FT', 'Fondant'), ('CR', 'Crema'), ('CH', 'Chocolate'), ('MR', 'Mermelada')], default='CR', max_length=2),
        ),
        migrations.AddField(
            model_name='pastel',
            name='image',
            field=models.ImageField(default=None, upload_to='pasteles'),
        ),
    ]