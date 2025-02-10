# Generated by Django 5.1.6 on 2025-02-08 02:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_restaurant'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='destination',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='restaurants', to='main_app.destination'),
        ),
    ]
