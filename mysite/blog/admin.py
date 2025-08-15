from django.contrib import admin
from .models import teacher, student, course

# Register your models here.
@admin.register(teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('teacher_name', 'teacher_reg','user')

# many to one relationship
@admin.register(student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'student_reg', 'user')
    
# many to many relationship
@admin.register(course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'course_reg', 'course_teacher')