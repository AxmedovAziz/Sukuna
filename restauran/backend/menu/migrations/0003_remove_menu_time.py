# Generated by Django 5.1 on 2024-08-24 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_menu_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='time',
        ),
    ]
