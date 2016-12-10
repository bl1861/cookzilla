from django.shortcuts import render

# Create your views here.

from .models import User,Conversion,Rsvp,Egroup,Event,GroupUser,Ingredient,Recipe,Related,Report,ReportPhoto,Review,ReviewPhoto,Tag
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
    groupUser=GroupUser(gid=group,uname= User.objects.get(uname='Rubby'))
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

def search_4(request):

    result = ''
    with connection.cursor() as cursor:
        cursor.execute("SELECT distinct Recipe.rid , Recipe.rtitle FROM Tag INNER JOIN Recipe on Tag.rid=Recipe.rid INNER JOIN Ingredient on Ingredient.rid=Recipe.rid INNER JOIN Conversion on Ingredient.cunit = Conversion.cunit WHERE Tag.tname ='cake' and Ingredient.iname LIKE '%suger%' and ((Ingredient.quantity)*(Conversion.cquantity)/Recipe.rserving) > 20")
        rows = cursor.fetchall()
    for row in rows:
        result += str(row[0])+' : ' + row[1]+'<br>'

    return HttpResponse(result)

def search_5(request):

    result = ''
    with connection.cursor() as cursor:
        cursor.execute("SELECT t1.r1, t1.avg_r FROM(SELECT Recipe.rid as r1, avg(Review.rating) as avg_r FROM Recipe INNER JOIN Review on Recipe.rid=Review.rid WHERE Recipe.rcontent ~* '[\s]tuna[\s]' GROUP BY Recipe.rid) as t1 ORDER BY t1.avg_r DESC")
        rows = cursor.fetchall()
    for row in rows:
        result += str(row[0])+' : ' + str(int(row[1])) + '<br>'

    return HttpResponse(result)

def update(request):

    cursor = connection.cursor()
    '''cursor.execute("INSERT INTO _User VALUES ( 'K.Smith', 'smith', '23456', 'good')")
    cursor.execute("INSERT INTO _User VALUES ( 'Bob','bb', '3456', 'nothing to say')")
    cursor.execute("INSERT INTO _User VALUES ( 'Michael Jack', 'Michael', '87654', 'I like to cook!')")
    cursor.execute("CREATE SEQUENCE serial_rk START 1")
    cursor.execute("INSERT INTO Recipe VALUES(nextval('serial_rk'),'cheese cake','Preheat oven to 325 degrees. For the filling, use your mixers lowest speed',2,'2016-10-09 12:15:24',null,'K.Smith')")
    cursor.execute("INSERT INTO Recipe VALUES(nextval('serial_rk'),'apple pie','Make the dough by hand. In a medium bowl, whisk together the flour, sugar, and salt',3,'2016-10-09 12:15:24',null,'Michael Jack')")
    cursor.execute("INSERT INTO Recipe VALUES(nextval('serial_rk'),'fried noodle','Bring a large pot of lightly salted water to a boil. Cook the egg noodles in the boiling water until the pasta is tender yet firm to the bite, about 5 minutes. Drain',2,'2016-10-09 12:15:24',null,'Bob')")
    cursor.execute("INSERT INTO _User VALUES ( 'Rubby', 'rbb', '23456', 'I like to cook!')")
    cursor.execute("INSERT INTO Recipe VALUES(nextval('serial_rk'),'beef pasta','Cook over medium heat for 5 minutes to slightly reduce. Add chopped spinach; cover skillet and simmer on reduced heat until spinach is tender',5,'2016-10-09 12:15:24',null,'Rubby')")
    cursor.execute("INSERT INTO Recipe VALUES(nextval('serial_rk'),'beef pasta','Use broccoli to make this pasta more delicious',5,'2016-10-09 12:15:24',null,'Rubby')")
    cursor.execute("INSERT INTO Recipe VALUES(nextval('serial_rk'),'Tuna Patties','These tuna patties is special!',5,'2016-10-09 12:15:24',null,'Bob')")
    cursor.execute("INSERT INTO Recipe VALUES(nextval('serial_rk'),'Grandma’s Fettuccini Alfredo','If you sift a little bit of cornstarch into your shredded cheese, and squeeze some fresh lemon juice into the sauce,it will become nice and creamy',5,'2016-10-09 12:15:24',null,'Michael Jack')")
    cursor.execute("INSERT INTO Recipe VALUES(1,'Grandma’s Fettuccini Alfredo','If you sift a little bit of cornstarch into your shredded cheese, and squeeze some fresh lemon juice into the sauce,it will become nice and creamy',5,'2016-10-09 12:15:24',null,'Michael Jack')")
    cursor.execute("INSERT INTO Tag VALUES(1,'dessert',1)")
    cursor.execute("INSERT INTO Tag VALUES(2,'dessert',2)")
    cursor.execute("INSERT INTO Tag VALUES(3,'cake',2)")
    cursor.execute("INSERT INTO Tag VALUES(4,'low fat',2)")
    cursor.execute("INSERT INTO Tag VALUES(5,'dessert',3)")
    cursor.execute("INSERT INTO Tag VALUES(6,'Vegan',3)")
    cursor.execute("INSERT INTO Tag VALUES(7,'low fat',3)")
    cursor.execute("INSERT INTO Recipe VALUES(4,'Grandma’s Fettuccini Alfredo','If you sift a little bit of cornstarch into your shredded cheese, and squeeze some fresh lemon juice into the sauce,it will become nice and creamy',5,'2016-10-09 12:15:24',null,'Michael Jack')")
    cursor.execute("INSERT INTO Recipe VALUES(6,'Grandma’s Fettuccini Alfredo','If you sift a little bit of cornstarch into your shredded cheese, and squeeze some fresh lemon juice into the sauce,it will become nice and creamy',5,'2016-10-09 12:15:24',null,'Michael Jack')")
    cursor.execute("INSERT INTO Tag VALUES(8,'beef',4)")
    cursor.execute("INSERT INTO Tag VALUES(9,'Asian',4)")
    cursor.execute("INSERT INTO Tag VALUES(10,'Italian',5)")
    cursor.execute("INSERT INTO Tag VALUES(11,'Healthy',5)")
    cursor.execute("INSERT INTO Tag VALUES(12,'Quick meal',5)")
    cursor.execute("INSERT INTO Tag VALUES(13,'Italian',6)")
    cursor.execute("INSERT INTO Ingredient VALUES(1,'egg',50.0,'ml',60.0,1)")
    cursor.execute("INSERT INTO Ingredient VALUES(2,'cream',50.0,'ml',60.0,1)")
    cursor.execute("INSERT INTO Ingredient VALUES(3,'eggs',2.0,'pc',5.0,1)")
    cursor.execute("INSERT INTO Ingredient VALUES(4,'butter',30.0,'grams',30.0,1)")
    cursor.execute("INSERT INTO Ingredient VALUES(5,'butter',30.0,'grams',30.0,1)")
    cursor.execute("INSERT INTO Ingredient VALUES(6,'suger',200.0,'grams',200.0,2)")
    cursor.execute("INSERT INTO Ingredient VALUES(7,'butter',40.0,'grams',40.0,2)")
    cursor.execute("INSERT INTO Ingredient VALUES(8,'apple',3.0,'pc',7.5,3)")
    cursor.execute("INSERT INTO Ingredient VALUES(9,'eggs',1.0,'pc',2.5,3)")
    cursor.execute("UPDATE Conversion set cquantity=1.2 where cunit='ml'")
    cursor.execute("INSERT INTO Conversion VALUES('pc',2.5)")
    cursor.execute("INSERT INTO Conversion VALUES('grams',1)")
    cursor.execute("INSERT INTO Review VALUES(2,'Bob','convenient recipe','eaasy and quick',5,6)")
    cursor.execute("INSERT INTO Review VALUES(3,'Bob','special choice','I like this elegant recipe',5,8)")
    cursor.execute("INSERT INTO Review VALUES(4,'K.Smith','good choice for dinner','I have been making homemade pasta for years. If I am going to be serving it the same day, I use cake flour.','like it',4,6)")
    cursor.execute("update Review set suggestion='good',rating=5,rid=6 where rwid=2")
    cursor.execute("update Review set suggestion='verygood',rating=5,rid=8 where rwid=3")
    cursor.execute("update recipe set rcontent='Use broccoli to make this pasta more delicious, adding some tuna is also recommend' where rid=6")
    cursor.execute("update egroup set gname='health diet' where gid=2")
    cursor.execute("update egroup set gname='Love cheese cake !' where gid=3")
    cursor.execute("update event set ename='how to cook effecienty',etime='2016-10-09 14:00:00' where eid=2")
    cursor.execute("update event set ename='new recipe for cake',etime='2016-10-09 11:12:00' where eid=3")
    cursor.execute("INSERT INTO egroup VALUES(1,'cook')")
    cursor.execute("INSERT INTO egroup VALUES(2,'happy')")
    cursor.execute("INSERT INTO egroup VALUES(3,'case')")
    cursor.execute("INSERT INTO event VALUES(1,'testt','2016-10-09 11:12:00',1)")
    cursor.execute("INSERT INTO event VALUES(2,'testt','2016-10-09 11:12:00',1)")
    cursor.execute("INSERT INTO event VALUES(3,'testt','2016-10-09 11:12:00',1)")
    cursor.execute("INSERT INTO rsvp VALUES(1,3,'Rubby')")
    cursor.execute("INSERT INTO rsvp VALUES(2,1,'Rubby')")
    cursor.execute("INSERT INTO rsvp VALUES(3,2,'Rubby')")'''


    result = 'update db successfully'

    return HttpResponse(result)
