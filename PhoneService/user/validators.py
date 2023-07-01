from django.core.exceptions import ValidationError
import re


def validate_phone(value):
    if not re.match(r'^(\+98|0)?9\d{9}$', value):
        raise ValidationError(
            '%(value)s is not an even number',
            params={'value': value},
        )


def validate_image(file_name):
    pass



