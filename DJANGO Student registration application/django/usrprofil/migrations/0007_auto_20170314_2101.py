# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-14 15:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usrprofil', '0006_auto_20170314_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='parent_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
