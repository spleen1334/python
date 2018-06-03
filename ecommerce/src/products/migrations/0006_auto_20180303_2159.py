# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-03 21:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20180303_2130'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='product',
            managers=[
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='slug'),
        ),
    ]