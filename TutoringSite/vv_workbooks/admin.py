from django.contrib import admin
# Resister custom models here.
from . models import VVWorkbook, VVExercise, VVExA, VVExParagraph


class VVWorkbookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'book')


class VVExAInline(admin.StackedInline):
    model = VVExA
    fields = ['picture_this', 'image_a', 'image_b']


class VVVVExParagraphInline(admin.StackedInline):
    model = VVExParagraph
    fields = ['paragraph']


class VVExerciseAdmin(admin.ModelAdmin):
    inlines = [VVVVExParagraphInline, VVExAInline]
    list_display = ('id', 'book', 'orig_num', 'title')


admin.site.register(VVWorkbook, VVWorkbookAdmin)
admin.site.register(VVExercise, VVExerciseAdmin)
