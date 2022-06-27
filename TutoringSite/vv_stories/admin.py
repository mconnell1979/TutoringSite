from django.contrib import admin
# Resister custom models here.
from . models import VVStoryBook, VVStory, VVStoryQuestion


class VVStoryBookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'book')


class VVStoryQuestionInline(admin.StackedInline):
    model = VVStoryQuestion
    extra = 1
    fields = ['question', ]


class VVStoryAdmin(admin.ModelAdmin):
    inlines = [VVStoryQuestionInline]
    list_display = ('id', 'book', 'number', 'story_type', 'title')


admin.site.register(VVStoryBook, VVStoryBookAdmin)
admin.site.register(VVStory, VVStoryAdmin)

