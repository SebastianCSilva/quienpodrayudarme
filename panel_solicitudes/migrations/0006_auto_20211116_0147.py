# Generated by Django 2.2.24 on 2021-11-16 04:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('panel_solicitudes', '0005_auto_20211116_0145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitudtarea',
            name='estado',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='panel_solicitudes.Estado'),
        ),
    ]
