from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
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
