# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-27 02:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0008_auto_20161127_0226'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='Location',
            new_name='location',
        ),
    ]
