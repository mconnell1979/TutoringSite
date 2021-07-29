from django.contrib import admin
from . models import LessonPlan, PersonalSightWord, LessonSightWordList


class LessonPlanAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'active', 'tutor', 'scheduled', 'updated',
                    'air_write_words', 'note',
                    )


class PersonalSightWordAdmin(admin.ModelAdmin):
    list_display = ('student', 'active', 'updated',
                    )


admin.site.register(LessonPlan, LessonPlanAdmin)
admin.site.register(PersonalSightWord, PersonalSightWordAdmin)
