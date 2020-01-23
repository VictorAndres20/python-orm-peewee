import datetime
from peewee import CharField, DoubleField, ForeignKeyField, DateTimeField
from src.entities.BaseModel import BaseModel
from src.entities.Enterprise import Enterprise

class Employee(BaseModel):
	#None of the fields are initialized with primary_key=True, an auto-incrementing primary key will automatically be created and named “id”
	username = CharField(max_length=255, unique=True)
	salary = DoubleField(default=0)
	created_date = DateTimeField(default=datetime.datetime.now)
	enterprise = ForeignKeyField(Enterprise, backref='employees')