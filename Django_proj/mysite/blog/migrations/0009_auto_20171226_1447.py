# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-26 08:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20171226_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_part',
            name='blogID',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Blog_Table'),
        ),
    ]
