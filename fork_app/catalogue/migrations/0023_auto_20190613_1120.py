# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-13 03:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0022_auto_20190601_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.FloatField(default=0, null=True, verbose_name='Rating'),
        ),
    ]
