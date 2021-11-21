from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveDestroyAPIView
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated

from relationship.models import Relationship
from . import serializers
from ..permissions import IsTeacherWrite


class RelationshipListCreateAPIView(ListCreateAPIView):
    queryset = Relationship.objects.all().order_by('-updated', '-created')
    permission_classes = (IsAuthenticated, IsTeacherWrite)

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return serializers.RelationshipRetrieveSerializer
        return serializers.RelationshipCreateSerializer


class RelationshipRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Relationship.objects.all()
    serializer_class = serializers.RelationshipRetrieveSerializer
    permission_classes = (IsAuthenticated,)


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
