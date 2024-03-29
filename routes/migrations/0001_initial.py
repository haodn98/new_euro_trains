# Generated by Django 5.0.1 on 2024-01-22 21:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cities', '0003_alter_city_options'),
        ('trains', '0002_alter_train_from_city_alter_train_to_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Route name')),
                ('overall_travel_time', models.PositiveSmallIntegerField(verbose_name='Overall time in a trip')),
                ('from_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='route_from_city_set', to='cities.city')),
                ('to_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='route_to_city_set', to='cities.city')),
                ('trains', models.ManyToManyField(to='trains.train', verbose_name='Trains list')),
            ],
            options={
                'verbose_name': 'Route',
                'verbose_name_plural': 'Routes',
                'ordering': ['overall_travel_time'],
            },
        ),
    ]
