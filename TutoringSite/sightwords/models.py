from django.db import models


class SightWord(models.Model):
    name = models.CharField(max_length=25, unique=True)
    orig_set = models.IntegerField()
    orig_num = models.IntegerField()

    def __str__(self):
        return "%s %s %s %s %s %s" % ('Set:', self.orig_set, '#', self.orig_num, ' - ', self.name)

    def __repr__(self):
        return '{self.__class__.__name__}(id={self.id}, {self.name}'.format(self=self)


class SightWordSentences(models.Model):
    sight_word = models.ManyToManyField(SightWord, blank=True)
    sentences = models.TextField(max_length=1000, blank=True, help_text="Sentences - Max 1000 characters")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s %s" % (str(self.id), self.sentences)

    def __repr__(self):
        return '{self.__class__.__name__}(id={self.id}, {self.sight_word1}'.format(self=self)
