from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import SAFE_METHODS

from lesson.models import Lesson
from . import serializers


class LessonListCreateAPIView(ListCreateAPIView):
    queryset = Lesson.objects.all().order_by('-updated', '-created')

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return serializers.LessonRetrieveSerializer
        return serializers.LessonCreateSerializer


class LessonRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return serializers.LessonRetrieveSerializer
        return serializers.LessonUpdateSerializer


class LessonListAPIView(ListAPIView):
    serializer_class = serializers.LessonRetrieveSerializer

    def get_queryset(self):
        if self.request.user.is_teacher:
            return Lesson.objects.filter(teacher=self.request.user).order_by('-updated', '-created')
        else:
            return Lesson.objects.filter(student=self.request.user).order_by('-updated', '-created')
