from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'student_email', 'locker_number']
    

all_students = Student.objects.all()
serializer = StudentSerializer(all_students, many=True)

class StudentAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        exclude = ['id']