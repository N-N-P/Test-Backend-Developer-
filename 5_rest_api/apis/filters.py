
# code here
import django_filters 
import FilterSet, filters
from .models import School, Classroom, Teacher, Student

class SchoolFilter(django_filters.FilterSet):
    class Meta:
        model = School
        fields = ['name']

class ClassroomFilter(django_filters.FilterSet):
    class Meta:
        model = Classroom
        fields = ['school']

class TeacherFilter(django_filters.FilterSet):
    class Meta:
        model = Teacher
        fields = ['classrooms', 'first_name', 'last_name', 'gender']

class StudentFilter(django_filters.FilterSet):
    class Meta:
        model = Student
        fields = ['classroom', 'first_name', 'last_name', 'gender']
