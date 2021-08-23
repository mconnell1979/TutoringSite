from django.contrib import admin
from . models import SightWord, SightWordSentences


class SightwordAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'orig_set', 'orig_num')


class SightwordSentencesAdmin(admin.ModelAdmin):
    list_display = ('id', 'sentences', 'created')


admin.site.register(SightWord, SightwordAdmin)
admin.site.register(SightWordSentences, SightwordSentencesAdmin)
