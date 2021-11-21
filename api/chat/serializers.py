from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from chat.models import Chat
from core.models import User
from relationship.models import Relationship


class ChatCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        read_only_fields = ('id', 'teacher_unread',  'student_unread', 'created', 'updated')
        fields = read_only_fields + ('student', 'teacher')

    def validate(self, attrs):
        attrs = super().validate(attrs)
        if not Relationship.objects.filter(student_id=attrs.get('student'), teacher_id=attrs.get('teacher')).exists():
            raise ValidationError({
                'student': 'There is no relationship between this teacher and student',
                'teacher': 'There is no relationship between this teacher and student'
            })
        if User.objects.get(pk=attrs.get('student')).is_teacher:
            raise ValidationError({'student': 'student is teacher'})
        if not User.objects.get(pk=attrs.get('teacher')).is_teacher:
            raise ValidationError({'teacher': 'teacher is student'})
        return attrs



class ChatRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        read_only_fields = ('id', 'student', 'teacher', 'teacher_unread',  'student_unread', 'created', 'updated')
        fields = read_only_fields


class ChatUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        read_only_fields = ('id', 'student', 'teacher', 'created', 'updated')
        fields = read_only_fields + ('teacher_unread',  'student_unread')
