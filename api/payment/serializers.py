from rest_framework import serializers

from payment.models import Payment


class PaymentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        read_only_fields = ('id', 'status', 'created', 'updated')
        fields = read_only_fields + ('cost',)


class PaymentRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        read_only_fields = ('id', 'status', 'cost', 'created', 'updated')
        fields = read_only_fields


class PaymentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        read_only_fields = ('id', 'created', 'updated')
        fields = read_only_fields + ('status', 'cost')
