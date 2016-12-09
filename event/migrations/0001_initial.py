# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-09 21:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Egroup',
            fields=[
                ('gid', models.AutoField(primary_key=True, serialize=False)),
                ('gname', models.CharField(max_length=50)),
            ],
            options={
                'managed': False,
                'db_table': 'egroup',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('eid', models.AutoField(primary_key=True, serialize=False)),
                ('ename', models.CharField(blank=True, max_length=30, null=True)),
                ('etime', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'event',
            },
        ),
        migrations.CreateModel(
            name='GroupUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'managed': False,
                'db_table': 'group_user',
            },
        ),
        migrations.CreateModel(
            name='Rsvp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'managed': False,
                'db_table': 'rsvp',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('uname', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('login_name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('udescription', models.CharField(blank=True, max_length=200, null=True)),
                ('ufile', models.FileField(blank=True, null=True, upload_to='')),
                ('uphoto', models.FileField(blank=True, null=True, upload_to='')),
            ],
            options={
                'managed': False,
                'db_table': '_user',
            },
        ),
    ]
