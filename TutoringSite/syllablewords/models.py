from django.db import models


# Create your models here.
class SyllableWord(models.Model):
    name = models.CharField(max_length=15)
    type = models.CharField(max_length=15)
    orig_box = models.IntegerField()
    orig_book = models.IntegerField()
    orig_num = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s %s %s %s %s %s %s %s" % ('Box', self.orig_box, 'Book', self.orig_book, '#', self.orig_num, '-', self.name)

    def __repr__(self):
        return '{self.__class__.__name__}(id={self.id}, {self.type}'.format(self=self)


class MultiSyllableWord(models.Model):
    name = models.CharField(max_length=15)
    type = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s %s %s %s" % (
        '#', self.id, '-', self.name)

    def __repr__(self):
        return '{self.__class__.__name__}(id={self.id}, {self.type}'.format(self=self)


class Affix(models.Model):
    name = models.CharField(max_length=15)
    type = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s %s %s %s" % (
        '#', self.id, '-', self.name)

    def __repr__(self):
        return '{self.__class__.__name__}(id={self.id}, {self.type}'.format(self=self)