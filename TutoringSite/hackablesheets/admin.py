from django.contrib import admin
from . models import HackableWordSet, HackableSentenceSet, HackableBook


class HackableBookAdmin(admin.ModelAdmin):
    list_display = ('title', 'orig_book')


class HackableWordSetAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'book', 'orig_num')


class HackableSentenceSetAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'book', 'orig_num')


admin.site.register(HackableBook, HackableBookAdmin)
admin.site.register(HackableWordSet, HackableWordSetAdmin)
admin.site.register(HackableSentenceSet, HackableSentenceSetAdmin)