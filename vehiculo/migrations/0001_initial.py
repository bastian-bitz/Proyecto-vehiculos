# Generated by Django 4.0.5 on 2024-12-13 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(choices=[('Fiat', 'Fiat'), ('Chevrolet', 'Chevrolet'), ('Ford', 'Ford'), ('Toyota', 'Toyota')], default='Ford', max_length=20)),
                ('modelo', models.CharField(max_length=100)),
                ('Serial_carroceria', models.CharField(max_length=50)),
                ('Serial_motor', models.CharField(max_length=50)),
                ('categoria', models.CharField(choices=[('Particular', 'Particular'), ('Transporte', 'Transporte'), ('Carga', 'Carga')], default='Particular', max_length=20)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha_fabricacion', models.DateField()),
                ('fecha_modificacion', models.DateField(auto_now=True)),
            ],
        ),
    ]
