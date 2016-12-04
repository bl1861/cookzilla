from django.shortcuts import render

# Create your views here.

from .models import User,Conversion,Rsvp,Egroup,Event,GroupUser,Ingredient,Photo,Recipe,Related,Report,ReportPhoto,Review,ReviewPhoto,Tag
from django.http import HttpResponse
from django.db import connection

# Create your views here.
def create_mydb(request):

    user=User(uname='Jack Smith', login_name='jack', password='12345', udescription='humorous')
    user.save()
    user=User(uname='Rubby', login_name='rb', password='23456', udescription='cute')
    user.save()

    conversion=Conversion(cunit='ml',cquantity=1)
    conversion.save()

    egroup=Egroup(gname='Happy birthday')
    egroup.save()

    group = Egroup.objects.get(gid=1)

    event=Event(gid=group, ename='Droup team discussion', etime='2016-10-09 12:15:24')
    event.save()

    groupUser=GroupUser(gid=group,uname=User.objects.get(uname='Jack Smith'))
    groupUser.save()

    e_dummy = Event.objects.get(eid=1)

    photo=Photo()
    photo.save()

    recipe=Recipe(uname=User.objects.get(uname='Jack Smith'),rtitle='ice cream',rcontent='5 easy steps',rserving=5)
    recipe.save()
    recipe=Recipe(uname=User.objects.get(uname='Rubby'),rtitle='ice cream',rcontent='2 easy steps',rserving=5)
    recipe.save()

    r_dummy = Recipe.objects.get(rid=1)
    r_dummy1 = Recipe.objects.get(rid=2)

    ingredient=Ingredient(rid=r_dummy,iname='cream',quantity=50.0,cunit='ml',gunit=60.0)
    ingredient.save()

    related=Related(rid=r_dummy,related=r_dummy1)
    related.save()

    report=Report(eid=1,uname=User.objects.get(uname='Jack Smith'),rdescription='It is really useful class !' )
    report.save()

    '''reportPhoto=ReportPhoto()
    reportPhoto.save()'''

    review=Review(rid=r_dummy,uname=User.objects.get(uname='Jack Smith'),rwtitle='good recipe',rwcontext='Very good recipe though I tweaked it a bit',suggestion='good',rating=4)
    review.save()

    '''reviewPhoto=ReviewPhoto()
    reviewPhoto.save()'''

    rsvp=Rsvp(uname=User.objects.get(uname='Jack Smith'),eid=e_dummy)
    rsvp.save()

    tag=Tag(rid=r_dummy,tname='dessert')
    tag.save()

    result = '<p>create model done<\p>'

    return HttpResponse(result)

def search_1(request):

    result = ''
    with connection.cursor() as cursor:
        cursor.execute("SELECT recipe.rid, recipe.rtitle FROM tag INNER JOIN recipe on Tag.rid=Recipe.rid WHERE Recipe.rcontent LIKE '%asy%' and lower(Tag.tname)='dessert'")
        rows = cursor.fetchall()
    for row in rows:
        result += str(row[0]) + row[1] + '<br>'

    return HttpResponse(result)

def search_2(request):

    result = ''
    with connection.cursor() as cursor:
        cursor.execute("SELECT t1.uname FROM(SELECT RSVP.uname as uname, count(*) as number FROM RSVP INNER JOIN Event on RSVP.eid = EVENT.eid INNER JOIN EGroup on EVENT.gid = EGroup.gid WHERE EGroup.gname = 'Happy birthday' group by RSVP.uname) as t1 WHERE t1.number >= 0;")
        rows = cursor.fetchall()
    for row in rows:
        result += str(row[0]) + '<br>'

    return HttpResponse(result)

def search_3(request):

    result = ''
    with connection.cursor() as cursor:
        cursor.execute("SELECT Related.related_id FROM Recipe INNER JOIN Related on Recipe.rid=Related.rid WHERE Recipe.rcontent ~* '[\s]easy[\s]'")
        rows = cursor.fetchall()
    for row in rows:
        result += str(row[0]) + '<br>'

    return HttpResponse(result)

def insert_1(request):

    result = ''
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO _User VALUES ( 'Bob','bb', '3456', 'nothing to say')")
        rows = cursor.fetchall()
    for row in rows:
        result += str(row[0]) + '<br>'

    return HttpResponse(result)
