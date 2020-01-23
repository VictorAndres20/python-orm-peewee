from peewee import CharField
from src.entities.BaseModel import BaseModel

class Enterprise(BaseModel):
	name = CharField(max_length=300, unique=True)