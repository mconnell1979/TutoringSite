from . models import SyllableWord, MultiSyllableWord, Affix
from django.contrib import admin


class SyllablewordAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'type', 'orig_box', 'orig_book', 'orig_num')


class MultiSyllablewordAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'type')


class AffixAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'type')


admin.site.register(SyllableWord, SyllablewordAdmin)
admin.site.register(MultiSyllableWord, MultiSyllablewordAdmin)
admin.site.register(Affix, AffixAdmin)