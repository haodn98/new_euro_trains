# Generated by Django 5.0.1 on 2024-01-20 22:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0002_alter_city_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ['name'], 'verbose_name_plural': 'Cities'},
        ),
    ]
