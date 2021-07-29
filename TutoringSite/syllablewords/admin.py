from django.contrib import admin
from . models import SyllableWord


class SyllablewordAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'type', 'orig_box', 'orig_book', 'orig_num')


admin.site.register(SyllableWord, SyllablewordAdmin)