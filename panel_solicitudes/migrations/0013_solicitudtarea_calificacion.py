# Generated by Django 2.2.24 on 2021-12-07 04:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('panel_solicitudes', '0012_auto_20211207_0105'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitudtarea',
            name='calificacion',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to='panel_solicitudes.Calificacion'),
        ),
    ]