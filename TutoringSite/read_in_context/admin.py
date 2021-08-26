from django.contrib import admin
from . models import SRABook, SRAPassage
from import_export.admin import ImportExportModelAdmin


class SRABookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


class SRAPassageAdmin(ImportExportModelAdmin):
    list_display = ('id', 'book', 'unit_num')


admin.site.register(SRABook, SRABookAdmin)
admin.site.register(SRAPassage, SRAPassageAdmin)
