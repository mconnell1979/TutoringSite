from django.db import models

class Grade(models.IntegerChoices):
    NEW = 0
    SNAIL = 1
    BIKE = 2
    JET = 3
    GRADUATE = 4