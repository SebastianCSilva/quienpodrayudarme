# Generated by Django 2.2.24 on 2021-11-16 04:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('panel_solicitudes', '0006_auto_20211116_0147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfilmaestro',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
