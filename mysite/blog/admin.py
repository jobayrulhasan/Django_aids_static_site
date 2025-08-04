from django.contrib import admin
from .models import teacher, student

# Register your models here.
@admin.register(teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('teacher_name', 'teacher_reg','user')

@admin.register(student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'student_reg', 'user')