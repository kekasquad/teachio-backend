from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import SAFE_METHODS

from note.models import Note
from . import serializers


class NoteListCreateAPIView(ListCreateAPIView):
    queryset = Note.objects.all().order_by('-updated', '-created')

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return serializers.NoteRetrieveSerializer
        return serializers.NoteCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class NoteRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return serializers.NoteRetrieveSerializer
        return serializers.NoteUpdateSerializer


class NoteListAPIView(ListAPIView):
    serializer_class = serializers.NoteRetrieveSerializer

    def get_queryset(self):
        if self.request.user.is_teacher:
            return Note.objects.filter(user=self.request.user).order_by('-updated', '-created')
