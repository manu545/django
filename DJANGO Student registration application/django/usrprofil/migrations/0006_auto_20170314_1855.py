# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-14 13:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usrprofil', '0005_auto_20170312_1842'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='birth_date',
            new_name='birthdate',
        ),
    ]
