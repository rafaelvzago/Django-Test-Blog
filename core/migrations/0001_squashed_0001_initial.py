# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-03 20:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [(b'core', '0001_initial')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
            ],
        ),
    ]