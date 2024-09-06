from rest_framework import generics, viewsets
from courses.models import Subject, Course
from courses.api.serializers import CourseSerializer
from django.db.models import Count
from courses.api.pagination import StandardPagePagination
from courses.api.serializers import SubjectSerializer
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from courses.api.permissions import IsEnrolled
from courses.api.serializers import CourseWithContentsSerializer
from rest_framework.authentication import SessionAuthentication, TokenAuthentication

class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.prefetch_related('modules')

    @action(
        detail=True,
        methods=['post'],
        authentication_classes=[BasicAuthentication],
        permission_classes=[IsAuthenticated]
    )
    def enroll(self, request, *args, **kwargs):
        course = self.get_object()
        course.student.add(request.user)
        return Response({'enrolled': True})

    @action(
        detail=True,
        methods=['get'],
        authentication_classes=[BasicAuthentication],
        serializer_class=CourseWithContentsSerializer,
        permission_classes=[IsAuthenticated, IsEnrolled]
    )
    def contents(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)



class SubjectViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = SubjectSerializer
    pagination_class = StandardPagePagination
    queryset = Subject.objects.prefetch_related('courses')


# class CoursesEnrollView(APIView):
#     authentication_classes = [SessionAuthentication, TokenAuthentication]
#     permission_classes = [IsAuthenticated]
#
#     def post(self, request, pk, format=None):
#         course = get_object_or_404(Course, pk=pk)
#         course.student.add(request.user)
#         return Response({'enrolled': True})
# class SubjectListView(generics.ListAPIView):
#     queryset = Subject.objects.annotate(total_courses=Count('courses'))
#     serializer_class = SubjectSerializer
#     pagination_class = StandardPagePagination
#
#
# class SubjectDetailView(generics.RetrieveAPIView):
#     queryset = Subject.objects.annotate(total_courses=Count('courses'))
#     serializer_class = SubjectSerializer