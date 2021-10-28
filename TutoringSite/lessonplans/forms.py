from django import forms
from django.forms import widgets
from .models import LessonPlan


class LessonPlanForm(forms.ModelForm):
    class Meta:
        model = LessonPlan
        fields = [
            'scheduled',
            'student',
            'tutor',
            'scheduled',
            'active',
            'sight_word_list',
            'syllable_word_list',
            'multisyllable_word_list',
            'affix_word_list',
            'hackable_word_set_list',
            'hackable_sentence_set_list',
            'air_write_words',
            'note',
        ]

        widgets = {
            'sight_word_list': forms.SelectMultiple(attrs={'size': 15}),
            'syllable_word_list': forms.SelectMultiple(attrs={'size': 15}),
            'multisyllable_word_list': forms.SelectMultiple(attrs={'size': 15}),
            'affix_word_list': forms.SelectMultiple(attrs={'size': 15}),
            'hackable_word_set_list': forms.SelectMultiple(attrs={'size': 5}),
            'hackable_sentence_set_list': forms.SelectMultiple(attrs={'size': 5}),
            'air_write_words': forms.Textarea(attrs={'class': 'textarea', 'rows': 2, 'placeholder': 'word_1, word_2, etc...'}),
            'note': forms.Textarea(attrs={'class': 'textarea', 'rows': 6, 'placeholder': 'notes...'}),
            'scheduled': widgets.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

# class LessonPlanForm(forms.Form):
#     model_choices = forms.ModelMultipleChoiceField(
#         widget=forms.CheckboxSelectMultiple,
#         queryset=LessonPlan.objects.all(),
#         initial=0
#     )
#     sight_word_start = forms.IntegerField()
#     sight_word_end = forms.IntegerField()
