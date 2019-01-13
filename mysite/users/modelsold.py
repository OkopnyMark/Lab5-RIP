from django.db import models
import MySQLdb

class Connection:
    def __init__(self, user, password, db, host='localhost'):
        self.user = user
        self.password = password
        self.host = host
        self.db = db
        self._connection = None

    @property
    def connection(self):
        return self._connection
    
    def __enter__(self):
        self.connect()
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()
    
    def connect(self):
        if not self._connection:
            self._connection = MySQLdb.connect(
                host = self.host,
                user = self.user,
                password = self.password,
                db = self.db
            )
    
    def disconnect(self):
        if self._connection:
            self._connection.close()

class Book:
    def __init__(self, db_connection, name, author, description):
        self.db_connection = db_connection.connection
        self.name = name
        self.author = author
        self.description = description
    
    def save(self):
        c = self.db_connection.cursor()
        c.execute("insert into books (name, author, description) values (%s, %s, %s);", (self.name, self.author, self.description))
        self.db_connection.commit()
        c.close()

class BookModel(models.Model):
    name = models.CharField(max_length = 100)
    author = models.CharField(max_length = 100)
    description = models.CharField(max_length = 200)
