# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-12 10:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usrprofil', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='location',
            new_name='address',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='profile',
            name='parent_name',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='profile',
            name='parent_phone',
            field=models.IntegerField(blank=True, default=10),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.IntegerField(blank=True, default=10),
        ),
        migrations.AddField(
            model_name='profile',
            name='pin',
            field=models.IntegerField(blank=True, default=7),
        ),
        migrations.AddField(
            model_name='profile',
            name='roll',
            field=models.IntegerField(blank=True, default=20),
        ),
    ]
