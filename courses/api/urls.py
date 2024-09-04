from django.urls import path, include
from rest_framework import routers
from . import views
from rest_framework.authtoken import views as v


router = routers.DefaultRouter()
router.register('courses', views.CourseViewSet)
router.register('subjects', views.SubjectViewSet)

app_name = 'courses'

urlpatterns = [
    path('', include(router.urls)),
    # path('courses/<pk>/enroll/', views.CoursesEnrollView.as_view(), name='course_enroll'),
]

