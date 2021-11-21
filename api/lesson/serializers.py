from rest_framework import serializers

from lesson.models import Lesson


class LessonCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        read_only_fields = ('id', 'payment_status', 'created', 'updated')
        fields = read_only_fields + ('cost', 'title', 'description', 'start', 'end', 'student', 'teacher')


class LessonRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        read_only_fields = ('id', 'payment_status', 'cost', 'title', 'description', 'start', 'end', 'student', 'teacher')
        fields = read_only_fields


class LessonUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        read_only_fields = ('id', 'created', 'updated', 'teacher')
        fields = read_only_fields + ('payment_status', 'cost', 'title', 'description', 'start', 'end', 'student')
