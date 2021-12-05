from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from lesson.models import Lesson
from . import serializers


class FinanceListAPIView(ListAPIView):
    serializer_class = serializers.FinanceRetrieveSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if self.request.user.is_teacher:
            return Lesson.objects\
                .filter(teacher=self.request.user, payment_status=Lesson.PaymentStatus.CONFIRMED)\
                .order_by('-updated', '-created')
        else:
            return Lesson.objects\
                .filter(student=self.request.user, payment_status=Lesson.PaymentStatus.CONFIRMED)\
                .order_by('-updated', '-created')