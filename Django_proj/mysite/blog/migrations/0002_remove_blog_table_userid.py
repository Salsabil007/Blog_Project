# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-18 12:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog_table',
            name='userID',
        ),
    ]
