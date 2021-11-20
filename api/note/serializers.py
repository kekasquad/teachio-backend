from rest_framework import serializers

from note.models import Note


class NoteCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        read_only_fields = ('id', 'user')
        fields = read_only_fields + ('content',)


class NoteRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        read_only_fields = ('id', 'user', 'content')
        fields = read_only_fields


class NoteUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        read_only_fields = ('id', 'user')
        fields = read_only_fields + ('content',)
