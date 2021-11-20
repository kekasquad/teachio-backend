from django.urls import re_path
from . import views

urlpatterns = [
    re_path(
        r'^$',
        views.PaymentListCreateAPIView.as_view(),
        name='payment_list_create'
    ),
    re_path(
        r'^(?P<pk>[^/]+)/?$',
        views.PaymentRetrieveUpdateDestroyAPIView.as_view(),
        name='payment_retrieve_update_destroy'
    )
]