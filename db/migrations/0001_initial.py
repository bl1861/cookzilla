# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-04 21:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conversion',
            fields=[
                ('cunit', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('cquantity', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'conversion',
            },
        ),
        migrations.CreateModel(
            name='Egroup',
            fields=[
                ('gid', models.AutoField(primary_key=True, serialize=False)),
                ('gname', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'egroup',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('eid', models.AutoField(primary_key=True, serialize=False)),
                ('ename', models.CharField(blank=True, max_length=30, null=True)),
                ('etime', models.DateTimeField(blank=True, null=True)),
                ('gid', models.ForeignKey(blank=True, db_column='gid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='db.Egroup')),
            ],
            options={
                'db_table': 'event',
            },
        ),
        migrations.CreateModel(
            name='GroupUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gid', models.ForeignKey(db_column='gid', on_delete=django.db.models.deletion.DO_NOTHING, related_name='group_gid', to='db.Egroup')),
            ],
            options={
                'db_table': 'group_user',
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
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('pid', models.AutoField(primary_key=True, serialize=False)),
                ('pname', models.CharField(blank=True, max_length=50, null=True)),
                ('img', models.BinaryField(blank=True, null=True)),
            ],
            options={
                'db_table': 'photo',
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('rid', models.AutoField(primary_key=True, serialize=False)),
                ('rtitle', models.CharField(blank=True, max_length=100, null=True)),
                ('rcontent', models.CharField(blank=True, max_length=200, null=True)),
                ('rserving', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'recipe',
            },
        ),
        migrations.CreateModel(
            name='Related',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('related', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='db.Recipe')),
                ('rid', models.ForeignKey(db_column='rid', on_delete=django.db.models.deletion.DO_NOTHING, related_name='relate_rid', to='db.Recipe')),
            ],
            options={
                'db_table': 'related',
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
            },
        ),
        migrations.CreateModel(
            name='ReportPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.ForeignKey(db_column='pid', on_delete=django.db.models.deletion.DO_NOTHING, to='db.Photo')),
                ('rpid', models.ForeignKey(db_column='rpid', on_delete=django.db.models.deletion.DO_NOTHING, to='db.Report')),
            ],
            options={
                'db_table': 'report_photo',
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
                ('rid', models.ForeignKey(blank=True, db_column='rid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='review_rid', to='db.Recipe')),
            ],
            options={
                'db_table': 'review',
            },
        ),
        migrations.CreateModel(
            name='ReviewPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.ForeignKey(db_column='pid', on_delete=django.db.models.deletion.DO_NOTHING, to='db.Photo')),
                ('rwid', models.ForeignKey(db_column='rwid', on_delete=django.db.models.deletion.DO_NOTHING, to='db.Review')),
            ],
            options={
                'db_table': 'review_photo',
            },
        ),
        migrations.CreateModel(
            name='Rsvp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.ForeignKey(db_column='eid', on_delete=django.db.models.deletion.DO_NOTHING, related_name='rsvp_eid', to='db.Event')),
            ],
            options={
                'db_table': 'rsvp',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tname', models.CharField(max_length=50)),
                ('rid', models.ForeignKey(db_column='rid', on_delete=django.db.models.deletion.DO_NOTHING, related_name='tag_rid', to='db.Recipe')),
            ],
            options={
                'db_table': 'tag',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('uname', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('login_name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('udescription', models.CharField(blank=True, max_length=200, null=True)),
                ('ufile', models.BinaryField(blank=True, null=True)),
            ],
            options={
                'db_table': '_user',
            },
        ),
        migrations.AddField(
            model_name='rsvp',
            name='uname',
            field=models.ForeignKey(db_column='uname', on_delete=django.db.models.deletion.DO_NOTHING, related_name='rsvp_uname', to='db.User'),
        ),
        migrations.AddField(
            model_name='report',
            name='uname',
            field=models.ForeignKey(db_column='uname', on_delete=django.db.models.deletion.DO_NOTHING, related_name='report_uname', to='db.User'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='uname',
            field=models.ForeignKey(blank=True, db_column='uname', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='recipe_uname', to='db.User'),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='rid',
            field=models.ForeignKey(blank=True, db_column='rid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='ing_rid', to='db.Recipe'),
        ),
        migrations.AddField(
            model_name='groupuser',
            name='uname',
            field=models.ForeignKey(blank=True, db_column='uname', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='group_user_uname', to='db.User'),
        ),
        migrations.AlterUniqueTogether(
            name='tag',
            unique_together=set([('rid', 'tname')]),
        ),
        migrations.AlterUniqueTogether(
            name='rsvp',
            unique_together=set([('uname', 'eid')]),
        ),
        migrations.AlterUniqueTogether(
            name='reviewphoto',
            unique_together=set([('rwid', 'pid')]),
        ),
        migrations.AlterUniqueTogether(
            name='reportphoto',
            unique_together=set([('rpid', 'pid')]),
        ),
        migrations.AlterUniqueTogether(
            name='related',
            unique_together=set([('rid', 'related')]),
        ),
        migrations.AlterUniqueTogether(
            name='groupuser',
            unique_together=set([('uname', 'gid')]),
        ),
    ]
