from django.contrib import admin
from . models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'dob','email', 'created')


admin.site.register(Student, StudentAdmin)