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
    uphoto = models.FileField(blank=True, null=True)

    class Meta:
        db_table = '_user'


class Conversion(models.Model):
    cunit = models.CharField(primary_key=True, max_length=50)
    cquantity = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'conversion'



class Egroup(models.Model):
    gid = models.AutoField(primary_key=True)
    gname = models.CharField(max_length=50)

    class Meta:
        db_table = 'egroup'


class Event(models.Model):
    eid = models.AutoField(primary_key=True)
    gid = models.ForeignKey(Egroup, models.DO_NOTHING, db_column='gid', blank=True, null=True)
    ename = models.CharField(max_length=30, blank=True, null=True)
    etime = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'event'


class GroupUser(models.Model):
    gid = models.ForeignKey(Egroup, models.DO_NOTHING, db_column='gid',related_name='group_gid')
    uname = models.ForeignKey(User, models.DO_NOTHING, db_column='uname',related_name='group_user_uname', blank=True, null=True)

    class Meta:
        db_table = 'group_user'
        unique_together = (('uname', 'gid'),)


class Ingredient(models.Model):
    igid = models.AutoField(primary_key=True)
    rid = models.ForeignKey('Recipe', models.DO_NOTHING, db_column='rid',related_name='ing_rid', blank=True, null=True)
    iname = models.CharField(max_length=30, blank=True, null=True)
    quantity = models.FloatField(blank=True, null=True)
    cunit = models.CharField(max_length=50, blank=True, null=True)
    gunit = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'ingredient'


'''class Photo(models.Model):
    pid = models.AutoField(primary_key=True)
    pname = models.CharField(max_length=50, blank=True, null=True)
    img = models.BinaryField(blank=True, null=True)

    class Meta:
        db_table = 'photo'
'''

class Recipe(models.Model):
    rid = models.AutoField(primary_key=True)
    uname = models.ForeignKey(User, models.DO_NOTHING, db_column='uname',related_name='recipe_uname', blank=True, null=True)
    rtitle = models.CharField(max_length=100)
    rcontent = models.CharField(max_length=200)
    rserving = models.IntegerField(blank=True, null=True)
    rtime = models.DateField()
    rphoto = models.FileField(blank=True, null=True)

    class Meta:

        db_table = 'recipe'


class Related(models.Model):
    rid = models.ForeignKey(Recipe, models.DO_NOTHING, db_column='rid',related_name='relate_rid')
    related = models.ForeignKey(Recipe, models.DO_NOTHING)

    class Meta:
        db_table = 'related'
        unique_together = (('rid', 'related'),)


class Report(models.Model):
    rpid = models.AutoField(primary_key=True)
    eid = models.ForeignKey(Event, models.DO_NOTHING, db_column='eid', related_name='report_eid')
    uname = models.ForeignKey(User, models.DO_NOTHING, db_column='uname',related_name='report_uname')
    rdescription = models.CharField(max_length=100, blank=True, null=True)

    class Meta:

        db_table = 'report'


class ReportPhoto(models.Model):
    rpid = models.ForeignKey(Report, models.DO_NOTHING, db_column='rpid')
    rp_photo_name = models.CharField(max_length=50, blank=True, null=True)
    rp_photo = models.FileField(blank=True, null=True)

    class Meta:
        db_table = 'report_photo'
        unique_together = (('rpid', 'rp_photo_name'),)


class Review(models.Model):
    rwid = models.AutoField(primary_key=True)
    rid = models.ForeignKey(Recipe, models.DO_NOTHING, db_column='rid',related_name='review_rid', blank=True, null=True)
    uname = models.ForeignKey(User, models.DO_NOTHING, db_column='uname',related_name='review_uname')
    rwtitle = models.CharField(max_length=100, blank=True, null=True)
    rwcontext = models.CharField(max_length=300, blank=True, null=True)
    suggestion = models.CharField(max_length=300, blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'review'


class ReviewPhoto(models.Model):
    rwid = models.ForeignKey(Review, models.DO_NOTHING, db_column='rwid')
    rw_photo_name = models.CharField(max_length=50, blank=True, null=True)
    rw_photo = models.FileField(blank=True, null=True)

    class Meta:

        db_table = 'review_photo'
        unique_together = (('rwid', 'rw_photo_name'),)


class Rsvp(models.Model):

    uname = models.ForeignKey(User, models.DO_NOTHING, db_column='uname',related_name='rsvp_uname')
    eid = models.ForeignKey(Event, models.DO_NOTHING, db_column='eid',related_name='rsvp_eid')

    class Meta:
        db_table = 'rsvp'
        unique_together = (('uname', 'eid'),)


class Tag(models.Model):
    rid = models.ForeignKey(Recipe, models.DO_NOTHING, db_column='rid',related_name='tag_rid')
    tname = models.CharField(max_length=50)

    class Meta:
        db_table = 'tag'
        unique_together = (('rid', 'tname'),)


class UserRecipeHistory(models.Model):
    uname = models.ForeignKey(User, models.DO_NOTHING, db_column='uname',related_name='visit_uname')
    rid = models.ForeignKey(Recipe, models.DO_NOTHING, db_column='rid',related_name='visit_rid')
    visit_time = models.DateField()

    class Meta:
        db_table = 'user_recipe_history'
        unique_together = (('uname', 'rid'),)

class UserTagHistory(models.Model):
    uname = models.ForeignKey(User, models.DO_NOTHING, db_column='uname',related_name='tag_uname')
    tname = models.CharField(max_length=50)
    tag_time = models.DateField()

    class Meta:
        db_table = 'user_tag_history'
        unique_together = (('uname', 'tname'),)

class UserKeyWordHistory(models.Model):
    uname = models.ForeignKey(User, models.DO_NOTHING, db_column='uname',related_name='keyword_uname')
    keyword = models.CharField(max_length=50)
    key_time = models.DateField()

    class Meta:
        db_table = 'user_keyword_history'
        unique_together = (('uname', 'keyword'),)