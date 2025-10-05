from django.contrib import admin
from .models import Student,StdSubjects

# Register your models here.
class StudentAdded(admin.TabularInline):
    model= StdSubjects
    extra=2
admin.site.register(Student)
admin.site.register(StdSubjects)