from django.core.exceptions import ValidationError
import re


def validate_subject_format(subject_name):
    error_message = "Subject must be in title case format."

    regex = r'^(?:[A-Z][a-z]*)(?:\s[A-Z][a-z]*)*$'

    good_subject = re.match(regex, subject_name)

    if not good_subject:
        raise ValidationError(error_message, params={'subject_name': subject_name})


def validate_professor_name(professor):
    error_message = 'Professor name must be in the format "Professor Adam".'

    regex = r'^Professor [A-Z][a-z]*$'

    good_professor = re.match(regex, professor)

    if not good_professor:
        raise ValidationError(error_message, params={'professor': professor})



