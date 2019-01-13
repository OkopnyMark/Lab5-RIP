from django.db import models
import MySQLdb
# Create your models here.

class Film(models.Model):
    name = models.CharField(max_length = 100)
    genre = models.CharField(max_length = 100)
    issue = models.CharField(max_length = 10)
    director = models.CharField(max_length = 100)
    description = models.CharField(max_length = 200)    

class Hall(models.Model):
    typehall = models.CharField(max_length = 10)
    seatsnumber = models.IntegerField()

class Session(models.Model):
    filmid = models.ForeignKey(Film, on_delete=models.PROTECT)
    hallid = models.ForeignKey(Hall, on_delete=models.PROTECT)
    startdt = models.DateTimeField()
    form = models.CharField(max_length = 3, default = '2D')

class Ticket(models.Model):
    sessionid = models.ForeignKey(Session, on_delete=models.PROTECT)
    cond = models.CharField(max_length = 10, default = 'free')
    price = models.CharField(max_length = 10, default = '100 rub')

#con = Connection('dbuser', '123', 'test_db')
#with con:
#    book = Book(con, 'qwerty', 'qwe', '123')
#    book.save()