from django.http import Http404
from rest_framework import status
from rest_framework.generics import  ListAPIView, RetrieveDestroyAPIView, GenericAPIView, CreateAPIView
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated
from rest_framework.response import Response

from core.models import StudentNote
from relationship.models import Relationship
from . import serializers
from ..permissions import IsTeacher, IsRelationshipParticipant


class RelationshipCreateAPIView(CreateAPIView):
    queryset = Relationship.objects.all().order_by('-updated', '-created')
    serializer_class = serializers.RelationshipCreateSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        relationship = serializer.save()

        StudentNote(
            teacher=relationship.teacher,
            student=relationship.student,
            description=""
        ).save()


class RelationshipRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Relationship.objects.all()
    serializer_class = serializers.RelationshipRetrieveSerializer
    permission_classes = (IsAuthenticated, IsRelationshipParticipant)

    def perform_destroy(self, instance):
        StudentNote.objects.get(
            student=instance.student,
            teacher=instance.teacher,
        ).delete()

        super().perform_destroy(instance)

    def get_object(self):
        try:
            return Relationship.objects.get(
                teacher=self.kwargs['teacher_id'],
                student=self.kwargs['student_id'],
            )
        except Relationship.DoesNotExist:
            raise Http404


class RelationshipListAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.RelationshipRetrieveSerializer

    def get_queryset(self):
        if self.request.user.is_teacher:
            return Relationship.objects.filter(
                teacher=self.request.user
            ).order_by('-updated', '-created')
        else:
            return Relationship.objects.filter(
                student=self.request.user
            ).order_by('-updated', '-created')


class RelationshipLinkAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated, IsTeacher)

    def get(self, request, *args, **kwargs):
        return Response(
            {'link': f'teachio://teacher_invite/{request.user.id}/'},
            status=status.HTTP_200_OK
        )