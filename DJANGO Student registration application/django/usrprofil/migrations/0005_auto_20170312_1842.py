# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-12 13:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usrprofil', '0004_auto_20170312_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='parent_phone',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='pin',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='roll',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
