from django.db import models


class VVPictureBook(models.Model):
    title = models.CharField(max_length=100, help_text="Sentence by Sentence")
    book = models.CharField(max_length=10, help_text="A")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s %s %s %s" % ('Book', self.book, '-', self.title)

    def __repr__(self):
        return '{self.__class__.__name__}(id={self.id}, {self.book}'.format(self=self)


class VVPicture(models.Model):
    book = models.ForeignKey(VVPictureBook, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, help_text="Title Of The Image")
    directions = models.TextField(
        help_text="Look at the picture before the lesson. Present the picture to the student. Say, Here is the pic...")
    image = models.ImageField(upload_to="images/vv_pictures/")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % (self.title,)

    def __repr__(self):
        return '{self.__class__.__name__}(id={self.id}, {self.title},'.format(self=self)


class VVPictureQuestion(models.Model):
    story = models.ForeignKey(VVPicture, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, help_text="Question to the whole.")
    number = models.IntegerField(help_text="Question Order #")
    question = models.TextField(help_text="a. Start at top. \r For example: What should I picture for the dog's face"
                                          "b. Use choice and contrast. \r For Example:Should I picture the dog with...")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % (self.title,)

    def __repr__(self):
        return '{self.__class__.__name__}(id={self.id},'.format(self=self)
