from django.db import models

class SRABook(models.Model):
    title = models.CharField(max_length=200, help_text="Getting the Main Idea")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s %s %s %s" % ('Book', self.orig_book, '-', self.title)

    def __repr__(self):
        return '{self.__class__.__name__}(id={self.id}, {self.orig_book}'.format(self=self)


class SRAPassage(models.Model):
    book = models.ForeignKey(SRABook, on_delete=models.CASCADE)
    unit_num = models.IntegerField(help_text="Unit #")
    passage = models.TextField(max_length=1000, help_text="Passage or Paragraph - Max 1000 characters")
    question = models.CharField(max_length=255, help_text="What is the main idea?")
    choiceA = models.CharField(max_length=255)
    choiceB = models.CharField(max_length=255)
    choiceC = models.CharField(max_length=255)
    choiceD = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

    def __repr__(self):
        return '{self.__class__.__name__}(id={self.id}, {self.student})'.format(self=self)