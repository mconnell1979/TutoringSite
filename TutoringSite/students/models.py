from django.db import models


# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    dob = models.DateField()
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s %s %s %s %s" % ('StudID:', self.id, '-', self.first_name, self.last_name)

    def __repr__(self):
        return '{self.__class__.__name__}(id={self.id}, {self.first_name}, {self.last_name})'.format(self=self)