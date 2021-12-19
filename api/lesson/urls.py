from django.urls import re_path
from . import views

urlpatterns = [
    re_path(
        r'^user/?$',
        views.LessonListAPIView.as_view(),
        name='user_lessons_list'
    ),
    re_path(
        r'^$',
        views.LessonCreateAPIView.as_view(),
        name='lesson_create'
    ),
    re_path(
        r'^(?P<pk>[^/]+)/payment-confirmation-request?$',
        views.LessonPaymentConfirmationRequestView.as_view(),
        name='lesson_payment_confirmation_request'
    ),
    re_path(
        r'^(?P<pk>[^/]+)/?$',
        views.LessonRetrieveUpdateDestroyAPIView.as_view(),
        name='lesson_retrieve_update_destroy'
    ),
]
