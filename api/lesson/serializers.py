from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from lesson.models import Lesson
from relationship.models import Relationship


class LessonCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        read_only_fields = ('id', 'payment_status', 'created', 'updated')
        fields = read_only_fields + (
            'cost', 'title', 'description', 'start', 'end', 'student', 'teacher', 'homework'
        )

    def validate(self, attrs):
        attrs = super().validate(attrs)
        if not Relationship.objects.filter(
                student_id=attrs.get('student'),
                teacher_id=attrs.get('teacher')
        ).exists():
            raise ValidationError({
                'student': 'There is no relationship between this teacher and student',
                'teacher': 'There is no relationship between this teacher and student'
            })
        return attrs


class LessonRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        read_only_fields = (
            'id', 'payment_status', 'cost', 'title', 'description',
            'start', 'end', 'student', 'teacher', 'homework'
        )
        fields = read_only_fields


class LessonUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        read_only_fields = ('id', 'created', 'updated', 'teacher')
        fields = read_only_fields + (
            'payment_status', 'cost', 'title', 'description', 'start', 'end', 'student', 'homework'
        )
