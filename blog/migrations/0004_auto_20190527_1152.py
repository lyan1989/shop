# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-27 03:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_content_html'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='nv',
            new_name='uv',
        ),
    ]