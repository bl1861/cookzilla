# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-11 05:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0004_auto_20161210_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertaghistory',
            name='tname',
            field=models.CharField(max_length=50),
        ),
    ]
