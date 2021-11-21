from rest_framework import serializers

from relationship.models import Relationship


class RelationshipCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relationship
        read_only_fields = ('created', 'updated')
        fields = read_only_fields + ('student', 'teacher')


class RelationshipRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relationship
        read_only_fields = ('student', 'teacher')
        fields = read_only_fields
