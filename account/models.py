# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class User(models.Model):
    uname = models.CharField(primary_key=True, max_length=50)
    login_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    udescription = models.CharField(max_length=200, blank=True, null=True)
    ufile = models.FileField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_user'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Conversion(models.Model):
    cunit = models.CharField(primary_key=True, max_length=50)
    cquantity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'conversion'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Egroup(models.Model):
    gid = models.AutoField(primary_key=True)
    gname = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'egroup'


class Event(models.Model):
    eid = models.AutoField(primary_key=True)
    ename = models.CharField(max_length=30, blank=True, null=True)
    etime = models.DateTimeField(blank=True, null=True)
    gid = models.ForeignKey(Egroup, models.DO_NOTHING, db_column='gid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event'


class GroupUser(models.Model):
    uname = models.CharField(max_length=50)
    gid = models.ForeignKey(Egroup, models.DO_NOTHING, db_column='gid')

    class Meta:
        managed = False
        db_table = 'group_user'
        unique_together = (('uname', 'gid'),)


class Ingredient(models.Model):
    igid = models.AutoField(primary_key=True)
    iname = models.CharField(max_length=30, blank=True, null=True)
    quantity = models.FloatField(blank=True, null=True)
    cunit = models.CharField(max_length=50, blank=True, null=True)
    gunit = models.FloatField(blank=True, null=True)
    rid = models.ForeignKey('Recipe', models.DO_NOTHING, db_column='rid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ingredient'


class Photo(models.Model):
    pid = models.AutoField(primary_key=True)
    pname = models.CharField(max_length=50, blank=True, null=True)
    img = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'photo'


class Recipe(models.Model):
    rid = models.AutoField(primary_key=True)
    rtitle = models.CharField(max_length=100, blank=True, null=True)
    rcontent = models.CharField(max_length=200, blank=True, null=True)
    rserving = models.IntegerField(blank=True, null=True)
    uname = models.ForeignKey(User, models.DO_NOTHING, db_column='uname', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recipe'


class Related(models.Model):
    related = models.ForeignKey(Recipe, models.DO_NOTHING,related_name='relate_rid')
    rid = models.ForeignKey(Recipe, models.DO_NOTHING, db_column='rid')

    class Meta:
        managed = False
        db_table = 'related'
        unique_together = (('rid', 'related'),)


class Report(models.Model):
    rpid = models.AutoField(primary_key=True)
    eid = models.IntegerField()
    rdescription = models.CharField(max_length=100, blank=True, null=True)
    uname = models.ForeignKey(User, models.DO_NOTHING, db_column='uname')

    class Meta:
        managed = False
        db_table = 'report'


class ReportPhoto(models.Model):
    pid = models.ForeignKey(Photo, models.DO_NOTHING, db_column='pid')
    rpid = models.ForeignKey(Report, models.DO_NOTHING, db_column='rpid')

    class Meta:
        managed = False
        db_table = 'report_photo'
        unique_together = (('rpid', 'pid'),)


class Review(models.Model):
    rwid = models.AutoField(primary_key=True)
    uname = models.CharField(max_length=50, blank=True, null=True)
    rwtitle = models.CharField(max_length=100, blank=True, null=True)
    rwcontext = models.CharField(max_length=200, blank=True, null=True)
    suggestion = models.CharField(max_length=100, blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    rid = models.ForeignKey(Recipe, models.DO_NOTHING, db_column='rid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'review'


class ReviewPhoto(models.Model):
    pid = models.ForeignKey(Photo, models.DO_NOTHING, db_column='pid')
    rwid = models.ForeignKey(Review, models.DO_NOTHING, db_column='rwid')

    class Meta:
        managed = False
        db_table = 'review_photo'
        unique_together = (('rwid', 'pid'),)


class Rsvp(models.Model):
    eid = models.ForeignKey(Event, models.DO_NOTHING, db_column='eid')
    uname = models.ForeignKey(User, models.DO_NOTHING, db_column='uname')

    class Meta:
        managed = False
        db_table = 'rsvp'
        unique_together = (('uname', 'eid'),)


class Tag(models.Model):
    tname = models.CharField(max_length=50)
    rid = models.ForeignKey(Recipe, models.DO_NOTHING, db_column='rid')

    class Meta:
        managed = False
        db_table = 'tag'
        unique_together = (('rid', 'tname'),)
