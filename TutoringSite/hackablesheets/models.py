from django.db import models


class HackableBook(models.Model):
    title = models.CharField(max_length=100, help_text="i.e. VC & CCV")
    orig_book = models.IntegerField(help_text="original book # 1-6")

    def __str__(self):
        return "%s %s %s %s" % ('Book #:', self.orig_book, 'Title', self.title)

    def __repr__(self):
        return '{self.__class__.__name__}(id={self.id}, {self.orig_book}'.format(self=self)


class HackableWordSet(models.Model):
    book = models.ForeignKey(HackableBook, on_delete=models.CASCADE)
    title = models.CharField(max_length=60, blank=True,  help_text="Sheet Title - i.e. CCV")
    subtitle = models.CharField(max_length=60, blank=True, help_text="i.e. some easy initial blends")
    note_top = models.CharField(max_length=100, blank=True, help_text="i.e. Finger Break and Read")
    note_bottom = models.CharField(max_length=500, blank=True, help_text="i.e. Remember: Try to start a syllable...")
    order = models.IntegerField(unique=True, help_text="unique consecutive #")
    orig_num = models.IntegerField(help_text="original sheet #")
    word1 = models.CharField(max_length=25, blank=True)
    word2 = models.CharField(max_length=25, blank=True)
    word3 = models.CharField(max_length=25, blank=True)
    word4 = models.CharField(max_length=25, blank=True)
    word5 = models.CharField(max_length=25, blank=True)
    word6 = models.CharField(max_length=25, blank=True)
    word7 = models.CharField(max_length=25, blank=True)
    word8 = models.CharField(max_length=25, blank=True)
    word9 = models.CharField(max_length=25, blank=True)
    word10 = models.CharField(max_length=25, blank=True)
    word11 = models.CharField(max_length=25, blank=True)
    word12 = models.CharField(max_length=25, blank=True)
    word13 = models.CharField(max_length=25, blank=True)
    word14 = models.CharField(max_length=25, blank=True)
    word15 = models.CharField(max_length=25, blank=True)
    word16 = models.CharField(max_length=25, blank=True)
    word17 = models.CharField(max_length=25, blank=True)
    word18 = models.CharField(max_length=25, blank=True)
    word19 = models.CharField(max_length=25, blank=True)
    word20 = models.CharField(max_length=25, blank=True)

    def __str__(self):
        return "%s %s %s %s %s %s" % ('Book:', self.book, '#', self.orig_num, 'Sheet id', self.order)

    def __repr__(self):
        return '{self.__class__.__name__}(id={self.id}, {self.book}, {self.orig_num},'.format(self=self)


class HackableSentenceSet(models.Model):
    book = models.ForeignKey(HackableBook, on_delete=models.CASCADE)
    title = models.CharField(max_length=60, blank=True, help_text="Sheet Title - i.e. CCV")
    subtitle = models.CharField(max_length=60, blank=True, help_text="i.e. some easy initial blends")
    note_top = models.CharField(max_length=100, blank=True, help_text="i.e. Finger Break and Read")
    note_bottom = models.CharField(max_length=500, blank=True,
                                   help_text="i.e. Remember: Try to start a syllable...")
    order = models.IntegerField(unique=True)
    orig_num = models.IntegerField()
    word1 = models.CharField(max_length=25, blank=True)
    word2 = models.CharField(max_length=25, blank=True)
    word3 = models.CharField(max_length=25, blank=True)
    word4 = models.CharField(max_length=25, blank=True)
    word5 = models.CharField(max_length=25, blank=True)
    word6 = models.CharField(max_length=25, blank=True)
    word7 = models.CharField(max_length=25, blank=True)
    word8 = models.CharField(max_length=25, blank=True)
    word9 = models.CharField(max_length=25, blank=True)
    word10 = models.CharField(max_length=25, blank=True)
    sentence1 = models.CharField(max_length=100, blank=True)
    sentence2 = models.CharField(max_length=100, blank=True)
    sentence3 = models.CharField(max_length=100, blank=True)
    sentence4 = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return "%s %s %s %s %s %s" % ('Book:', self.book, '#', self.orig_num, 'Sheet id', self.order)

    def __repr__(self):
        return '{self.__class__.__name__}(id={self.id}, {self.orig_book}, {self.orig_num},'.format(self=self)
