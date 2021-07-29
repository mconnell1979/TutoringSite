from django.db import models


# Create your models here.
class SightWord(models.Model):
    name = models.CharField(max_length=25, unique=True)
    order = models.IntegerField(unique=True)
    orig_set = models.IntegerField()
    orig_num = models.IntegerField()

    def __str__(self):
        return "%s %s %s %s %s %s" % ('Set:', self.orig_set, '#', self.orig_num, ' - ', self.name)
        # return self.name

