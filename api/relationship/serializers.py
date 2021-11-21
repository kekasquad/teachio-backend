from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from relationship.models import Relationship


class RelationshipCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relationship
        read_only_fields = ('created', 'updated')
        fields = read_only_fields + ('student', 'teacher')

    def validate(self, attrs):
        attrs = super().validate(attrs)
        if attrs.get('student').is_teacher:
            raise ValidationError({'student': 'student is teacher'})
        if not attrs.get('teacher').is_teacher:
            raise ValidationError({'teacher': 'teacher is student'})
        return attrs


class RelationshipRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relationship
        read_only_fields = ('student', 'teacher')
        fields = read_only_fields
