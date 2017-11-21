# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-21 16:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog_Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=200, unique=True)),
                ('blog_slug', models.CharField(max_length=200, unique=True)),
                ('creation_timestamp', models.DateField(auto_now_add=True, db_index=True)),
                ('modified_timestamp', models.DateField(auto_now_add=True, db_index=True)),
                ('blog_body', models.TextField()),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
