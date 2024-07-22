from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=255, blank=False)
    student_email = models.EmailField(max_length=255, unique=True, blank=False)
    personal_email = models.EmailField(blank=True, unique=True, max_length=255)
    locker_number = models.IntegerField(blank=False, unique=True, default=110)
    locker_combination = models.CharField(max_length=8, blank=False, default="12-12-12")
    good_student = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - {self.student_email} - {self.locker_number}"
    
    def locker_reassignment(self):
        new_locker_number = input('What is the new locker number?')
        self.locker_number = new_locker_number
        self.save()

    def student_status(self):
        self.good_student = not self.good_student