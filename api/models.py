from django.db import models
from datetime import datetime
date = datetime.strptime

# Create your models here.

class City(models.Model):
	city = models.CharField(max_length=100, blank = False, null = False)

class Publisher(models.Model):
    name = models.CharField(max_length=100, blank = False, null = False)
    city = models.ForeignKey(City)
    phone = models.CharField(max_length=100, blank = False, null = False)

class Journal(models.Model):
	index = models.IntegerField(unique = True)
	name = models.CharField(max_length=100, blank = False, null = False)
	number = models.IntegerField()
	price = models.FloatField()
	publisher = models.ForeignKey(Publisher)

class Subscriber(models.Model):
	name = models.CharField(max_length=100, blank = False, null = False)
	address = models.CharField(max_length=1000, blank = False, null = False)

class Subscribtion(models.Model):
	journal = models.ForeignKey(Journal)
	subscriber = models.ForeignKey(Subscriber)
	start_date = models.DateField()
	end_date = models.DateField()

def db_fill():
	d = City(city = "Donetsk")
	d.save()
	k = City(city = "Kiev"   )
	k.save()
	m = City(city = "Moskow" )
	m.save()

	p1 = Publisher(name = "North", city = d, phone = '(099) 123-45-67')
	p1.save()
	p2 = Publisher(name = "South", city = d, phone = '(050) 456-78-90')
	p2.save()
	p3 = Publisher(name = "West",  city = k, phone = '(066) 789-01-23')
	p3.save()
	p4 = Publisher(name = "East",  city = k, phone = '(078) 012-34-56')
	p4.save()

	j1  = Journal(index = 1,  number = 10000,   price = 7.8,   publisher = p1, name = 'January'  )
	j1.save()
	j2  = Journal(index = 2,  number = 100000,  price = 2.5,   publisher = p1, name = 'Febrary'  )
	j2.save()
	j3  = Journal(index = 3,  number = 20000,   price = 3.14,  publisher = p1, name = 'March'    )
	j3.save()
	j4  = Journal(index = 4,  number = 25000,   price = 0.8,   publisher = p2, name = 'April'    )
	j4.save()
	j5  = Journal(index = 5,  number = 1000,    price = 22.85, publisher = p2, name = 'May'      )
	j5.save()
	j6  = Journal(index = 6,  number = 50000,   price = 3.8,   publisher = p2, name = 'June'     )
	j6.save()
	j7  = Journal(index = 7,  number = 175000,  price = 6.8,   publisher = p3, name = 'July'     )
	j7.save()
	j8  = Journal(index = 8,  number = 500,     price = 55.34, publisher = p3, name = 'August'   )
	j8.save()
	j9  = Journal(index = 9,  number = 20000,   price = 5.59,  publisher = p3, name = 'September')
	j9.save()
	j10 = Journal(index = 10, number = 100000,  price = 6.12,  publisher = p4, name = 'October'  )
	j10.save()
	j11 = Journal(index = 11, number = 500000,  price = 11.20, publisher = p4, name = 'November' )
	j11.save()
	j12 = Journal(index = 12, number = 1000000, price = 1.40,  publisher = p4, name = 'December' )
	j12.save()
	
	s1 = Subscriber(name = 'Ivan', address = 'CCCP')
	s1.save()	
	s2 = Subscriber(name = 'Vasya', address = 'CCCP')
	s2.save()	
	s3 = Subscriber(name = 'Petya', address = 'CCCP')
	s3.save()	
	s4 = Subscriber(name = 'Masha', address = 'CCCP')
	s4.save()	
	s5 = Subscriber(name = 'Kolya', address = 'CCCP')
	s5.save()

	Subscribtion(journal = j1,  subscriber = s1, start_date = date('01-01-2003', '%d-%m-%Y'), end_date = date('31-12-2013', '%d-%m-%Y')).save()
	Subscribtion(journal = j2,  subscriber = s1, start_date = date('01-01-2003', '%d-%m-%Y'), end_date = date('31-12-2013', '%d-%m-%Y')).save()
	Subscribtion(journal = j1,  subscriber = s1, start_date = date('01-01-2003', '%d-%m-%Y'), end_date = date('31-12-2013', '%d-%m-%Y')).save()
	Subscribtion(journal = j2,  subscriber = s1, start_date = date('01-01-2003', '%d-%m-%Y'), end_date = date('31-12-2013', '%d-%m-%Y')).save()
	Subscribtion(journal = j1,  subscriber = s1, start_date = date('01-01-2003', '%d-%m-%Y'), end_date = date('31-12-2013', '%d-%m-%Y')).save()

	Subscribtion(journal = j1,  subscriber = s2, start_date = date('01-01-2003', '%d-%m-%Y'), end_date = date('31-12-2013', '%d-%m-%Y')).save()
	Subscribtion(journal = j3,  subscriber = s2, start_date = date('01-01-2003', '%d-%m-%Y'), end_date = date('31-12-2013', '%d-%m-%Y')).save()
	Subscribtion(journal = j4,  subscriber = s2, start_date = date('01-01-2003', '%d-%m-%Y'), end_date = date('31-12-2013', '%d-%m-%Y')).save()
	Subscribtion(journal = j5,  subscriber = s2, start_date = date('01-01-2003', '%d-%m-%Y'), end_date = date('31-12-2013', '%d-%m-%Y')).save()
	Subscribtion(journal = j6,  subscriber = s2, start_date = date('01-01-2003', '%d-%m-%Y'), end_date = date('31-12-2013', '%d-%m-%Y')).save()

	Subscribtion(journal = j7,  subscriber = s3, start_date = date('01-01-2003', '%d-%m-%Y'), end_date = date('31-12-2013', '%d-%m-%Y')).save()
	Subscribtion(journal = j7,  subscriber = s3, start_date = date('01-01-2003', '%d-%m-%Y'), end_date = date('31-12-2013', '%d-%m-%Y')).save()
	Subscribtion(journal = j7,  subscriber = s3, start_date = date('01-01-2003', '%d-%m-%Y'), end_date = date('31-12-2013', '%d-%m-%Y')).save()
	Subscribtion(journal = j7,  subscriber = s3, start_date = date('01-01-2003', '%d-%m-%Y'), end_date = date('31-12-2013', '%d-%m-%Y')).save()
	Subscribtion(journal = j7,  subscriber = s3, start_date = date('01-01-2003', '%d-%m-%Y'), end_date = date('31-12-2013', '%d-%m-%Y')).save()

	Subscribtion(journal = j5,  subscriber = s4, start_date = date('01-01-2003', '%d-%m-%Y'), end_date = date('31-12-2013', '%d-%m-%Y')).save()
	Subscribtion(journal = j3,  subscriber = s4, start_date = date('01-01-2003', '%d-%m-%Y'), end_date = date('31-12-2013', '%d-%m-%Y')).save()
	Subscribtion(journal = j1,  subscriber = s4, start_date = date('01-01-2003', '%d-%m-%Y'), end_date = date('31-12-2013', '%d-%m-%Y')).save()
	Subscribtion(journal = j2,  subscriber = s4, start_date = date('01-01-2003', '%d-%m-%Y'), end_date = date('31-12-2013', '%d-%m-%Y')).save()
	Subscribtion(journal = j7,  subscriber = s4, start_date = date('01-01-2003', '%d-%m-%Y'), end_date = date('31-12-2013', '%d-%m-%Y')).save()

	Subscribtion(journal = j8,  subscriber = s5, start_date = date('01-01-2003', '%d-%m-%Y'), end_date = date('31-12-2013', '%d-%m-%Y')).save()
	Subscribtion(journal = j1,  subscriber = s5, start_date = date('01-01-2003', '%d-%m-%Y'), end_date = date('31-12-2013', '%d-%m-%Y')).save()
	Subscribtion(journal = j3,  subscriber = s5, start_date = date('01-01-2003', '%d-%m-%Y'), end_date = date('31-12-2013', '%d-%m-%Y')).save()
	Subscribtion(journal = j4,  subscriber = s5, start_date = date('01-01-2003', '%d-%m-%Y'), end_date = date('31-12-2013', '%d-%m-%Y')).save()
	Subscribtion(journal = j12, subscriber = s5, start_date = date('01-01-2003', '%d-%m-%Y'), end_date = date('31-12-2013', '%d-%m-%Y')).save()

# db_fill();