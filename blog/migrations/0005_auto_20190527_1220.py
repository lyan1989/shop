# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-27 04:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190527_1152'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_time'], 'verbose_name': 'article', 'verbose_name_plural': 'article'},
        ),
    ]
