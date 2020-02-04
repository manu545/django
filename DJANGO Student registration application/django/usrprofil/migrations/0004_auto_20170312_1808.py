# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-12 12:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usrprofil', '0003_auto_20170312_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='parent_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='parent_phone',
            field=models.IntegerField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.IntegerField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='pin',
            field=models.IntegerField(blank=True, max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='roll',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
    ]
