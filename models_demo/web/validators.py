# 1. If valid - do nothing
# 2. If invalid - raise ValidationError('Some text')
from datetime import date

from django.core.exceptions import ValidationError


def validate_after_today(value):
    if date.today() < value:
        raise ValidationError(f"{value} is in the future")


def validate_over_18_years_old(value):
    if value < 18:
        raise ValidationError('You must be 18 in order to get hired')



