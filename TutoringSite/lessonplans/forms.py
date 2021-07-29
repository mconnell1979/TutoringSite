from django import forms
from .models import LessonPlan

class LessonPlanForm(forms.ModelForm):
    class Meta:
        model = LessonPlan
        fields = [
            'student',
            'active',
            'sight_word_list',
            'syllable_word_list',
            'air_write_words',
            'note',
        ]

        widgets = {
            'sight_word_list': forms.SelectMultiple(attrs={'size': 25}),
            'syllable_word_list': forms.SelectMultiple(attrs={'size': 25}),
            'air_write_words': forms.Textarea(attrs={'class': 'textarea', 'rows': 2, 'placeholder': 'word_1, word_2, etc...'}),
            'note': forms.Textarea(attrs={'class': 'textarea', 'rows': 6, 'placeholder': 'notes...'}),
        }

# class LessonPlanForm(forms.Form):
#     model_choices = forms.ModelMultipleChoiceField(
#         widget=forms.CheckboxSelectMultiple,
#         queryset=LessonPlan.objects.all(),
#         initial=0
#     )
#     sight_word_start = forms.IntegerField()
#     sight_word_end = forms.IntegerField()
