from django.db import models
from django.core.exceptions import ValidationError


def validate_string(value):
    if not isinstance(value, str):
        raise ValidationError("Only strings are allowed for this field.")


class Person(models.Model):
    name = models.CharField(max_length=100, unique=True, validators=validate_string)
