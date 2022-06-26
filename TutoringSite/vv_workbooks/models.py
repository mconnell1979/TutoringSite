from django.db import models


class VVWorkbook(models.Model):
    title = models.CharField(max_length=100, help_text="Sentence by Sentence")
    book = models.CharField(max_length=10, help_text="A")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s %s %s %s" % ('Book', self.book, '-', self.title)

    def __repr__(self):
        return '{self.__class__.__name__}(id={self.id}, {self.book}'.format(self=self)


class VVExercise(models.Model):
    book = models.ForeignKey(VVWorkbook, on_delete=models.CASCADE)
    orig_num = models.IntegerField(help_text="exercise #")
    title = models.CharField(max_length=60, help_text="The Snowstorm")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s %s %s" % (self.book, '#', self.orig_num)

    def __repr__(self):
        return '{self.__class__.__name__}(id={self.id}, {self.book}, {self.orig_num},'.format(self=self)


class VVExParagraph(models.Model):
    exercise = models.OneToOneField(VVExercise, primary_key=True, on_delete=models.CASCADE)
    paragraph = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % (self.paragraph,)

    def __repr__(self):
        return '{self.__class__.__name__}(id={self.id},'.format(self=self)


class VVExA(models.Model):
    exercise = models.OneToOneField(VVExercise, primary_key=True, on_delete=models.CASCADE)
    picture_this = models.CharField(max_length=200, help_text="Sometimes gray clouds and cold winds fill...")
    image_a = models.ImageField(upload_to="images/vv_workbook/")
    image_b = models.ImageField(upload_to="images/vv_workbook/")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % (self.picture_this,)

    def __repr__(self):
        return '{self.__class__.__name__}(id={self.id}, {self.picture_this},'.format(self=self)
