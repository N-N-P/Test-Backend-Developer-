from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apis import views

# ติดปัญหา ViewSet ไม่สามารถใช้งานได้
router = DefaultRouter()
# router.register(r'schools', views.SchoolViewSet, basename='school')
# router.register(r'classrooms', views.ClassroomViewSet, basename='classroom')
# router.register(r'teachers', views.TeacherViewSet, basename='teacher')
# router.register(r'students', views.StudentViewSet, basename='student')

urlpatterns = [
    path('v1/', include(router.urls))
]
