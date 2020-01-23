from peewee import Model
from src.config.db import db

class BaseModel(Model):
	class Meta:
		database = db