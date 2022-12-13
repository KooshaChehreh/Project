from django.core.exceptions import ValidationError


def validate_discount(value):
    if not 0 < value < 100:
        raise ValidationError('Discount should be between 0 - 100 percent')
