# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-26 08:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20171226_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_part',
            name='blogID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Blog_Table'),
        ),
    ]