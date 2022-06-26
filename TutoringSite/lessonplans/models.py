from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from students.models import Student
from sightwords.models import SightWord
from syllablewords.models import SyllableWord, MultiSyllableWord, Affix
from hackablesheets.models import HackableWordSet, HackableSentenceSet
from vv_stories.models import VVStory
from tutoringsite import choices


# Create your models here.
class LessonPlan(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    tutor = models.ForeignKey(User, models.SET_NULL, blank=True, null=True, help_text="assigned tutor to give lesson")
    scheduled = models.DateTimeField(blank=True, null=True, help_text="scheduled time for lesson to be given")
    sight_word_list = models.ManyToManyField(SightWord, blank=True, through='LessonSightWordList')
    syllable_word_list = models.ManyToManyField(SyllableWord, blank=True, through='LessonSyllableWordList')
    multisyllable_word_list = models.ManyToManyField(MultiSyllableWord, blank=True,
                                                     through='LessonMultiSyllableWordList')
    affix_word_list = models.ManyToManyField(Affix, blank=True, through='LessonAffixWordList')
    hackable_word_set_list = models.ManyToManyField(HackableWordSet, blank=True, through='LessonHackableWordSetList')
    hackable_sentence_set_list = models.ManyToManyField(HackableSentenceSet, blank=True,
                                                        through='LessonHackableSentenceSetList')
    air_write_words = models.TextField(max_length=200, blank=True, help_text="max 200 characters")
    vv_story = models.ManyToManyField(VVStory, blank=True, through='LessonVVStoryList')
    note = models.TextField(max_length=1000, blank=True, help_text="Notes for the tutor - Max 1000 characters")

    def __str__(self):
        return 'LessonID:' + str(self.id) + ' - ' + str(self.student) + ' - lesson updated: ' + str(self.updated)

    def __repr__(self):
        return '{self.__class__.__name__}(id={self.id}, {self.student})'.format(self=self)

    def get_absolute_url(self):
        return reverse("lessonplans:detail", kwargs={"pk": self.pk})


class PersonalSightWord(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    sight_word = models.ForeignKey(SightWord, on_delete=models.CASCADE)
    last_grade = models.IntegerField(choices=choices.Grade.choices, default=0)
    snail_num = models.IntegerField(default=0, help_text="# of times snail was scored")
    bike_num = models.IntegerField(default=0, help_text="# of times bike was scored")
    jet_num = models.IntegerField(default=0, help_text="# of times jet was scored")
    graduate_num = models.IntegerField(default=0, help_text="# of times graduate was scored")

    def __str__(self):
        return str(self.student) + ' ' + str(self.sight_word) + ' ' + str(self.last_grade)

    def __repr__(self):
        return '{self.__class__.__name__}(id={self.id}, {self.student}, {self.sight_word})'.format(self=self)


# Through Table - Lesson To Sight Word
class LessonSightWordList(models.Model):
    sight_word = models.ForeignKey(SightWord, on_delete=models.CASCADE)
    lesson_plan = models.ForeignKey(LessonPlan, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = [['sight_word', 'lesson_plan']]

    def __str__(self):
        return str(self.sight_word.name)

    def __repr__(self):
        return '{self.__class__.__name__}(id={self.id}, ' \
               '{self.student}, {self.sight_word}, ' \
               '{self.lesson_plan.id})'.format(self=self)


# Through Table - Lesson To Syllable Word
class LessonSyllableWordList(models.Model):
    syllable_word = models.ForeignKey(SyllableWord, on_delete=models.CASCADE)
    lesson_plan = models.ForeignKey(LessonPlan, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = [['syllable_word', 'lesson_plan']]

    def __str__(self):
        return str(self.syllable_word)


# Through Table - Lesson To Multi-Syllable Word
class LessonMultiSyllableWordList(models.Model):
    multisyllable_word = models.ForeignKey(MultiSyllableWord, on_delete=models.CASCADE)
    lesson_plan = models.ForeignKey(LessonPlan, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = [['multisyllable_word', 'lesson_plan']]

    def __str__(self):
        return str(self.multisyllable_word)


# Through Table - Lesson To Affix Word
class LessonAffixWordList(models.Model):
    affix_word = models.ForeignKey(Affix, on_delete=models.CASCADE)
    lesson_plan = models.ForeignKey(LessonPlan, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = [['affix_word', 'lesson_plan']]

    def __str__(self):
        return str(self.affix_word)


# Through Table - Lesson To Hackable Word Sheet
class LessonHackableWordSetList(models.Model):
    hackable_word_set = models.ForeignKey(HackableWordSet, on_delete=models.CASCADE)
    lesson_plan = models.ForeignKey(LessonPlan, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = [['hackable_word_set', 'lesson_plan']]

    def __str__(self):
        return str(self.hackable_word_set)

    def __repr__(self):
        return '{self.__class__.__name__}(id={self.id}, {self.hackable_word_set}, {self.lesson_plan},'.format(self=self)


# Through Table - Lesson To Hackable Sentence Sheet
class LessonHackableSentenceSetList(models.Model):
    hackable_sentence_set = models.ForeignKey(HackableSentenceSet, on_delete=models.CASCADE)
    lesson_plan = models.ForeignKey(LessonPlan, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = [['hackable_sentence_set', 'lesson_plan']]

    def __str__(self):
        return str(self.hackable_sentence_set)


# Through Table - Lesson To VV Story
class LessonVVStoryList(models.Model):
    vv_story = models.ForeignKey(VVStory, on_delete=models.CASCADE)
    lesson_plan = models.ForeignKey(LessonPlan, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = [['vv_story', 'lesson_plan']]

    def __str__(self):
        return str(self.vv_story)

    def __repr__(self):
        return '{self.__class__.__name__}(id={self.id}, {self.vv_story}, {self.lesson_plan},'.format(self=self)
