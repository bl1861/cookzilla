from __future__ import unicode_literals
from django.db import models


# Create your models here.

class User(models.Model):
    uname = models.CharField(primary_key=True, max_length=50)
    login_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    udescription = models.CharField(max_length=200, blank=True, null=True)
    ufile = models.FileField(blank=True, null=True)
    uphoto = models.FileField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_user'

class Egroup(models.Model):
    gid = models.AutoField(primary_key=True)
    gname = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'egroup'
        

class GroupUser(models.Model):
    uname = models.ForeignKey(User, models.DO_NOTHING, db_column='uname')
    gid = models.ForeignKey(Egroup, models.DO_NOTHING, db_column='gid')

    class Meta:
        managed = False
        db_table = 'group_user'
        unique_together = (('uname', 'gid'),)



class Event(models.Model):
    eid = models.AutoField(primary_key=True)
    ename = models.CharField(max_length=30, blank=True, null=True)
    etime = models.DateTimeField(blank=True, null=True)
    gid = models.ForeignKey(Egroup, models.DO_NOTHING, db_column='gid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event'


class Rsvp(models.Model):
    eid = models.ForeignKey(Event, models.DO_NOTHING, db_column='eid')
    uname = models.ForeignKey(User, models.DO_NOTHING, db_column='uname')

    class Meta:
        managed = False
        db_table = 'rsvp'
        unique_together = (('uname', 'eid'),)

