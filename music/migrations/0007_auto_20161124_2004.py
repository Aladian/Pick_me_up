# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-24 20:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_singup'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SingUp',
            new_name='SignUp',
        ),
    ]
