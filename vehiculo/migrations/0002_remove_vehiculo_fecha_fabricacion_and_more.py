# Generated by Django 4.0.5 on 2024-12-13 23:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehiculo',
            name='fecha_fabricacion',
        ),
        migrations.AddField(
            model_name='vehiculo',
            name='fecha_creacion',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
