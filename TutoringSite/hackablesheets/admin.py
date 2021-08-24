from django.contrib import admin
from . models import HackableWordSet, HackableSentenceSet, HackableBook
from import_export.admin import ImportExportModelAdmin


class HackableBookAdmin(admin.ModelAdmin):
    list_display = ('title', 'orig_book')


class HackableWordSetAdmin(ImportExportModelAdmin):
    list_display = ('id', 'title', 'subtitle', 'book', 'orig_num')


class HackableSentenceSetAdmin(ImportExportModelAdmin):
    list_display = ('id', 'title', 'subtitle', 'book', 'orig_num')


admin.site.register(HackableBook, HackableBookAdmin)
admin.site.register(HackableWordSet, HackableWordSetAdmin)
admin.site.register(HackableSentenceSet, HackableSentenceSetAdmin)