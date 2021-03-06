from rest_framework import status
from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView, ListAPIView, CreateAPIView, GenericAPIView
)
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated
from rest_framework.response import Response

from lesson.models import Lesson
from . import serializers
from ..permissions import IsTeacherWrite, IsStudent


class LessonCreateAPIView(CreateAPIView):
    queryset = Lesson.objects.all().order_by('-updated', '-created')
    serializer_class = serializers.LessonCreateSerializer
    permission_classes = (IsAuthenticated, IsTeacherWrite)


class LessonRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = (IsAuthenticated, IsTeacherWrite)

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return serializers.LessonRetrieveSerializer
        return serializers.LessonUpdateSerializer


class LessonListAPIView(ListAPIView):
    serializer_class = serializers.LessonRetrieveSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if self.request.user.is_teacher:
            return Lesson.objects.filter(teacher=self.request.user).order_by('-updated', '-created')
        else:
            return Lesson.objects.filter(student=self.request.user).order_by('-updated', '-created')


class LessonPaymentConfirmationRequestView(GenericAPIView):
    permission_classes = (IsAuthenticated, IsStudent,)

    def get_queryset(self):
        return Lesson.objects.filter(
            student=self.request.user,
            payment_status=Lesson.PaymentStatus.NOT_CONFIRMED
        )

    def post(self, request, *_, **__):
        lesson = self.get_object()
        lesson.payment_status = Lesson.PaymentStatus.REQUESTED
        lesson.save(update_fields=['payment_status'])
        return Response(status=status.HTTP_202_ACCEPTED)
