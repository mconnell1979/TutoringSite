from django.db import models


# Create your models here.
class SyllableWord(models.Model):
    objects = None
    name = models.CharField(max_length=15)
    order = models.IntegerField(unique=True)
    type = models.CharField(max_length=15)
    orig_box = models.IntegerField()
    orig_book = models.IntegerField()
    orig_num = models.IntegerField()

    def __str__(self):
        return "%s %s %s %s %s %s %s %s" % ('Box', self.orig_box, 'Book', self.orig_book, '#', self.orig_num, '-', self.name)
