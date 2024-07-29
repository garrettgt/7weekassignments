# Generated by Django 5.0.7 on 2024-07-28 01:10

import student_app.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0006_student_subjects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='locker_combination',
            field=models.CharField(default='12-12-12', max_length=10, validators=[student_app.validators.validate_combination_format]),
        ),
    ]
