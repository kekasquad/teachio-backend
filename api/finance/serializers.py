from rest_framework import serializers

from lesson.models import Lesson


class FinanceRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        read_only_fields = ('lesson_id', 'cost', 'time')
        fields = read_only_fields

    lesson_id = serializers.UUIDField(source='id', read_only=True)
    time = serializers.DateTimeField(source='end', read_only=True)
