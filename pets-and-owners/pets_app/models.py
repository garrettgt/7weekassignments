from django.db import models

# Create your models here.
# class Student(models.Model):
#     name = models.CharField(max_length=255, blank=False)
#     student_email = models.EmailField(max_length=255, unique=True, blank=False)
#     personal_email = models.EmailField(blank=True, unique=True, max_length=255)
#     locker_number = models.IntegerField(blank=False, unique=True, default=110)
#     locker_combination = models.CharField(max_length=8, blank=False, default="12-12-12")
#     good_student = models.BooleanField(default=True)

class Owner(models.Model):
    name = models.CharField(max_length=255, blank=False)
    age = models.BigIntegerField (blank=False)
    number_of_pets = models.BigIntegerField(blank=False)

class Cat(models.Model):
    breed = models.CharField(max_length=255)
    age = models.BigIntegerField
    vaccinated = models.BooleanField
    description = models.TextField(max_length=255)
    name = models.CharField(max_length=255)

class Dog(models.Model):
    age = models.BigIntegerField
    name = models.CharField(max_length=255)
    vaccinated = models.BooleanField
    breed = models.CharField(max_length=255)
    description = models.TextField(max_length=255)

class Bird(models.Model):
    name = models.CharField(max_length=255)
    age = models.BigIntegerField
    vaccinated = models.BooleanField
    description = models.TextField(max_length=255)
    species = models.CharField(max_length=255)

class Exotic_Animal(models.Model):
    region_of_origin = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    age = models.BigIntegerField
    type_of_animal = models.CharField
    vaccinated = models.BooleanField(blank=False)

