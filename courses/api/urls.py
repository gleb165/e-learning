from django.urls import path
from . import views

app_name = 'courses'

urlpattern = [
    path('/subject/', views.SubjectListView.as_view(), name='subject_list'),
    path('/subject/<pk>/', views.SubjectDetailView, name='subject_Detail'),
]