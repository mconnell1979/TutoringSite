from django.contrib import admin
# Resister custom models here.
from . models import VVPictureBook, VVPicture, VVPictureQuestion


class VVPictureBookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'book')


class VVPictureQuestionInline(admin.StackedInline):
    model = VVPictureQuestion
    fields = ['title', 'number', 'question']


class VVPictureAdmin(admin.ModelAdmin):
    inlines = [VVPictureQuestionInline]
    list_display = ('id', 'book', 'title')


admin.site.register(VVPictureBook, VVPictureBookAdmin)
admin.site.register(VVPicture, VVPictureAdmin)
