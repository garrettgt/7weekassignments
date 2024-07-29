from django.core.exceptions import ValidationError
import re

def validate_name_format(name):
    error_message = 'Name must be in the format "First Middle Initial. Last"'

    regex = r'^[A-Z][a-z]+ [A-Z]\. [A-Z][a-z]+$'

    good_name = re.match(regex, name)

    if not good_name:
        raise ValidationError(error_message, params={'name': name})


def validate_school_email(email):
    error_message = 'Invalid school email format. Please use an email ending with "@school.com".'

    if not email.endswith("@school.com"):
        raise ValidationError(error_message, params={'email': email})


def validate_combination_format(locker_combination):
    error_message = 'Combination must be in the format "12-12-12"'

    pattern = re.compile(r'^\d{2}-\d{2}-\d{2}$')

    if not pattern.match(locker_combination):
        raise ValidationError(error_message, params={'combination': locker_combination})

def validate_min_value(locker):
    error_message = "Ensure this value is greater than or equal to 1."

    if locker <= 0:
        raise ValidationError(error_message, params={'locker': locker})


def validate_max_value(locker):
    error_message = "Ensure this value is less than or equal to 200."

    if locker > 200:
        raise ValidationError(error_message, params={'locker': locker})
    
def validate_subjects(subjects):
    error_message1 = "This students class schedule is empty!"
    error_message2 = "This students class schedule is full!"

    if subjects <= 0:
        raise ValidationError(error_message1, params={'subjects': subjects})
    if subjects >= 8:
        raise ValidationError(error_message2, params={'subjects': subjects})