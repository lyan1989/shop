# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-27 02:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190525_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content_html',
            field=models.TextField(blank=True, editable=False, verbose_name='\u6b63\u6587html\u4ee3\u7801'),
        ),
    ]
