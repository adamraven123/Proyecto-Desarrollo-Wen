# Generated by Django 2.0.6 on 2018-06-21 02:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pastel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=240)),
                ('tipo', models.CharField(choices=[('MH', 'Milhojas'), ('BC', 'Bizcocho'), ('YG', 'Yogurt'), ('PQ', 'Panqueque'), ('HR', 'Hojarasca'), ('HL', 'Heladas'), ('MG', 'Merengue')], default='BC', max_length=10)),
                ('vegano', models.BooleanField(default=False)),
                ('celiaco', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PerfilUsuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('VE', 'Vendedor'), ('CL', 'Cliente'), ('AD', 'Administrador')], default='VE', max_length=2)),
                ('rut', models.IntegerField()),
                ('dv', models.CharField(default='', max_length=1)),
                ('fecha_creacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Pasteles',
        ),
        migrations.AddField(
            model_name='materia',
            name='tipo',
            field=models.CharField(choices=[('MP', 'Materia Prima'), ('IT', 'Ingrediente de Torta')], default='MP', max_length=2),
        ),
        migrations.AlterField(
            model_name='materia',
            name='cod',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='sabor',
            field=models.CharField(choices=[('CH', 'Chocolate'), ('MJ', 'Manjar'), ('NL', 'Nutella'), ('SN', 'Selva negra'), ('CP', 'Crema Pastelera'), ('TL', 'Tres Leches'), ('ML', 'Merengue Lucuma')], default='SN', max_length=10),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='tipo',
            field=models.CharField(choices=[('MH', 'Milhojas'), ('BC', 'Bizcocho'), ('YG', 'Yogurt'), ('PQ', 'Panqueque'), ('HR', 'Hojarasca'), ('HL', 'Heladas'), ('MG', 'Merengue')], default='BC', max_length=10),
        ),
        migrations.AlterField(
            model_name='stock',
            name='cantidad',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='stock',
            name='medida',
            field=models.CharField(choices=[('GR', 'Gramos'), ('CC', 'Centimetro cubico')], default='GR', max_length=2),
        ),
        migrations.AddField(
            model_name='pastel',
            name='sabor',
            field=models.ManyToManyField(blank=True, default=None, null=True, to='core.Materia'),
        ),
    ]
