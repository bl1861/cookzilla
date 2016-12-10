# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-10 00:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Conversion',
            fields=[
                ('cunit', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('cquantity', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'conversion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('igid', models.AutoField(primary_key=True, serialize=False)),
                ('iname', models.CharField(blank=True, max_length=30, null=True)),
                ('quantity', models.FloatField(blank=True, null=True)),
                ('cunit', models.CharField(blank=True, max_length=50, null=True)),
                ('gunit', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'ingredient',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('rid', models.AutoField(primary_key=True, serialize=False)),
                ('rtitle', models.CharField(blank=True, max_length=100, null=True)),
                ('rcontent', models.CharField(blank=True, max_length=200, null=True)),
                ('rserving', models.IntegerField(blank=True, null=True)),
                ('rtime', models.DateField()),
                ('rphoto', models.FileField(blank=True, null=True, upload_to='')),
            ],
            options={
                'db_table': 'recipe',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Related',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'related',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('rpid', models.AutoField(primary_key=True, serialize=False)),
                ('eid', models.IntegerField()),
                ('rdescription', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'report',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ReportPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rp_photo_name', models.CharField(blank=True, max_length=50, null=True)),
                ('rp_photo', models.FileField(blank=True, upload_to='')),
            ],
            options={
                'db_table': 'report_photo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('rwid', models.AutoField(primary_key=True, serialize=False)),
                ('uname', models.CharField(blank=True, max_length=50, null=True)),
                ('rwtitle', models.CharField(blank=True, max_length=100, null=True)),
                ('rwcontext', models.CharField(blank=True, max_length=200, null=True)),
                ('suggestion', models.CharField(blank=True, max_length=100, null=True)),
                ('rating', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'review',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ReviewPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rw_photo_name', models.CharField(blank=True, max_length=50, null=True)),
                ('rw_photo', models.FileField(blank=True, upload_to='')),
            ],
            options={
                'db_table': 'review_photo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tname', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'tag',
                'managed': False,
            },
        ),
    ]
