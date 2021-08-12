# from tkinter.messagebox import *
from peewee import *
import datetime

db = SqliteDatabase('ORM.db')


class BaseModel(Model):
    class Meta:
        database = db


class producto(BaseModel):
    titulo = CharField(unique=True)
    descripcion = TextField()
    fecha = DateTimeField(default=datetime.datetime.now)

    def __str__(self):
    	return ' Título y Descripción: ' + self.titulo + self.descripcion

db.connect()
db.create_tables([producto])

