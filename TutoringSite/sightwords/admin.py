from django.contrib import admin
from . models import SightWord


class SightwordAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'orig_set', 'orig_num')


admin.site.register(SightWord, SightwordAdmin)
