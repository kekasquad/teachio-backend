from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated

from core.models import StudentNote
from . import serializers
from ..permissions import IsTeacher


class StudentNoteRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = serializers.StudentNoteRetrieveUpdateSerializer
    permission_classes = (IsAuthenticated, IsTeacher)

    def get_object(self):
        return StudentNote.objects.get(
            teacher=self.request.user,
            student=self.kwargs['student_id']
        )
