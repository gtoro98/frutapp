from django.db import models

# Create your models here.
class Fruit(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.TextField()
	price = models.TextField()

class Costumer(models.Model):
	nombre = models.TextField()
	apellido = models.TextField()