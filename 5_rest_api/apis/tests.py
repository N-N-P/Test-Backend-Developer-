from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import School, Classroom, Teacher, Student

# Create your tests here.

class SchoolAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.school = School.objects.create(name="Test School", abbreviation="TS", address="123 Test St")

    def test_create_school(self):
        data = {"name": "New School", "abbreviation": "NS", "address": "456 New St"}
        response = self.client.post('/api/schools/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(School.objects.count(), 2)

    def test_list_schools(self):
        response = self.client.get('/api/schools/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_school_detail(self):
        response = self.client.get(f'/api/schools/{self.school.id}/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Test School")

    def test_update_school(self):
        data = {"name": "Updated School", "abbreviation": "US", "address": "123 Test St"}
        response = self.client.put(f'/api/schools/{self.school.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.school.refresh_from_db()
        self.assertEqual(self.school.name, "Updated School")

    def test_delete_school(self):
        response = self.client.delete(f'/api/schools/{self.school.id}/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(School.objects.count(), 0)