# Generated by Django 2.2.24 on 2021-10-27 05:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('panel_solicitudes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarea',
            name='id_categoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='panel_solicitudes.Categoria'),
        ),
    ]
