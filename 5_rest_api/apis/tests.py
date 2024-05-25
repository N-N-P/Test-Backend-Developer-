from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from rest_framework.test import APIClient
from .models import School, Classroom, Teacher, Student

class SchoolTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.school = School.objects.create(name="Test School", abbreviation="TS", address="123 Test St")

    def test_school_creation(self):
        self.assertEqual(School.objects.count(), 1)

    def test_school_api_list(self):
        response = self.client.get('/api/schools/')
        self.assertEqual(response.status_code, 200)

class ClassroomTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.school = School.objects.create(name="Test School", abbreviation="TS", address="123 Test St")
        self.classroom = Classroom.objects.create(grade=1, section=1, school=self.school)

    def test_classroom_creation(self):
        self.assertEqual(Classroom.objects.count(), 1)

    def test_classroom_api_list(self):
        response = self.client.get('/api/classrooms/')
        self.assertEqual(response.status_code, 200)

class TeacherTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.teacher = Teacher.objects.create(first_name="John", last_name="Doe", gender="M")

    def test_teacher_creation(self):
        self.assertEqual(Teacher.objects.count(), 1)

    def test_teacher_api_list(self):
        response = self.client.get('/api/teachers/')
        self.assertEqual(response.status_code, 200)

class StudentTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.school = School.objects.create(name="Test School", abbreviation="TS", address="123 Test St")
        self.classroom = Classroom.objects.create(grade=1, section=1, school=self.school)
        self.student = Student.objects.create(first_name="Jane", last_name="Doe", gender="F", classroom=self.classroom)

    def test_student_creation(self):
        self.assertEqual(Student.objects.count(), 1)

    def test_student_api_list(self):
        response = self.client.get('/api/students/')
        self.assertEqual(response.status_code, 200)
