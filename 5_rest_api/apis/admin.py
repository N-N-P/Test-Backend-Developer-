from django.contrib import admin

# Register your models here.
from .models import School, Classroom, Teacher, Student

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'abbreviation', 'address')
    search_fields = ('name', 'abbreviation')

@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ('grade', 'section', 'school')
    search_fields = ('grade', 'section')
    list_filter = ('school',)

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'gender')
    search_fields = ('first_name', 'last_name')
    list_filter = ('gender',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'gender', 'classroom')
    search_fields = ('first_name', 'last_name')
    list_filter = ('classroom', 'gender')
