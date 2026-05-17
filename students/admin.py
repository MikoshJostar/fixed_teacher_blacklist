
from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'student_class', 'debt', 'bad_grade', 'created_at')
    search_fields = ('name', 'student_class')
