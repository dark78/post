from django.db import models

# Create your models here.

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

class Journal(models.Model):
	index = models.IntegerField(max_length=100)
	name = models.CharField(max_length=100)
	number = models.IntegerField()
	price = models.FloatField()
	publisher = models.ForeignKey(Publisher)

class Subscriber(models.Model):
	name = models.CharField(max_length=100)
	address = models.CharField(max_length=100)
	journal = models.ManyToManyField(Journal)