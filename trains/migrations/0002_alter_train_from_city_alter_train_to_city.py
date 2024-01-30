# Generated by Django 5.0.1 on 2024-01-22 14:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0003_alter_city_options'),
        ('trains', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='train',
            name='from_city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_city_set', to='cities.city'),
        ),
        migrations.AlterField(
            model_name='train',
            name='to_city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_city_set', to='cities.city'),
        ),
    ]
