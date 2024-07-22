from django.db import models

# Create your models here.
class Client(models.Model):
    account_type = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    active = models.BooleanField(default=True)

class Video(models.Model):
    title = models.CharField(max_length=255)
    in_stock = models.BigIntegerField
    rating = models.CharField

class Person(models.Model):
    first_name = models.CharField
    last_name = models.CharField
    middle_init = models.CharField(blank=True)
    age = models.BigIntegerField

class Address(models.Model):
    street = models.CharField
    zipcode = models.BigIntegerField
    state = models.CharField
    appt_num = models.BigIntegerField(blank=True)

class Store(models.Model):
    name = models.CharField
    number_of_employees = models.BigIntegerField
    rating = models.FloatField
    owner = models.BigIntegerField