from django.db import models
from django.core.validators import RegexValidator

class Person(models.Model):
    name = models.CharField(max_length=100, unique=True, validators=[RegexValidator(r'^[a-zA-Z0-9]+$')])
