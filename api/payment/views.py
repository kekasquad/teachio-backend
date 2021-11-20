from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import SAFE_METHODS

from payment.models import Payment
from . import serializers


class PaymentListCreateAPIView(ListCreateAPIView):
    queryset = Payment.objects.all().order_by('-updated', '-created')

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return serializers.PaymentRetrieveSerializer
        return serializers.PaymentCreateSerializer


class PaymentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return serializers.PaymentRetrieveSerializer
        return serializers.PaymentUpdateSerializer