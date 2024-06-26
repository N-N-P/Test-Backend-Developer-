from rest_framework import serializers
from .models import School, Classroom, Teacher, Student

# code here

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class ClassroomSerializer(serializers.ModelSerializer):
    teachers = TeacherSerializer(many=True, read_only=True)
    students = StudentSerializer(many=True, read_only=True)

    class Meta:
        model = Classroom
        fields = '__all__'

class SchoolSerializer(serializers.ModelSerializer):
    classroom_count = serializers.IntegerField(source='classrooms.count', read_only=True)
    teacher_count = serializers.SerializerMethodField()
    student_count = serializers.SerializerMethodField()

    class Meta:
        model = School
        fields = '__all__'

    def get_teacher_count(self, obj):
        return Teacher.objects.filter(classrooms__school=obj).distinct().count()

    def get_student_count(self, obj):
        return Student.objects.filter(classroom__school=obj).count()