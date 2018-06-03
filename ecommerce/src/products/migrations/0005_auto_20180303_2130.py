# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-03 21:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20180303_2102'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='product',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
