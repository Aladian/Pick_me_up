# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-01 06:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='is_faborite',
            field=models.BooleanField(default=False),
        ),
    ]
