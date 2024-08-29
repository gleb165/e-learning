from rest_framework import generics
from courses.models import Subject
from django.db.models import Count
from courses.api.pagination import StandardPagePagination
from courses.api.serializers import SubjectSerializer


class SubjectListView(generics.ListAPIView):
    queryset = Subject.objects.annotate(total_courses=Count('courses'))
    serializer_class = SubjectSerializer
    pagination_class = StandardPagePagination


class SubjectDetailView(generics.RetrieveAPIView):
    queryset = Subject.objects.annotate(total_courses=Count('courses'))
    serializer_class = SubjectSerializer