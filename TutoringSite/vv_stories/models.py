from django.db import models


class VVStoryBook(models.Model):
    title = models.CharField(max_length=100, help_text="Imagine That! Stories")
    book = models.CharField(max_length=10, help_text="Grade 5")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s %s %s %s" % ('Book', self.book, '-', self.title)

    def __repr__(self):
        return '{self.__class__.__name__}(id={self.id}, {self.book}'.format(self=self)


class VVStory(models.Model):
    title = models.CharField(max_length=100, help_text="Imagine That! Stories")
    book = models.ForeignKey(VVStoryBook, on_delete=models.CASCADE)
    number = models.IntegerField(help_text="Story #")
    story = models.TextField(help_text="Write story here.")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('book', 'number',)

    def __str__(self):
        return "%s" "%s" "%s" "%s" "%s" "%s" % (self.book.title, ':', self.book.book, ' - ', self.number, self.title,)

    def __repr__(self):
        return '{self.__class__.__name__}(id={self.id},'.format(self=self)


class VVStoryQuestion(models.Model):
    story = models.ForeignKey(VVStory, on_delete=models.CASCADE)
    question = models.CharField(max_length=200, help_text="What is the main idea of the story?")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % (self.question,)

    def __repr__(self):
        return '{self.__class__.__name__}(id={self.id},'.format(self=self)
