from rest_framework import serializers

from core.models import StudentNote


class StudentNoteRetrieveUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentNote
        read_only_fields = ('student',)
        fields = read_only_fields + ('description',)
