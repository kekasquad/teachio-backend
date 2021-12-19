from django.urls import re_path
from fcm_django.api.rest_framework import FCMDeviceAuthorizedViewSet

from . import views

urlpatterns = [
    re_path(
        r'^current/?$',
        views.CurrentUserAPIView.as_view(),
        name='user_list'
    ),
    re_path(
        r'^devices/?$',
        FCMDeviceAuthorizedViewSet.as_view({'post': 'create'}),
        name='create_fcm_device'
    ),
    re_path(
        r'^(?P<pk>[^/]+)/?$',
        views.UserRetrieveUpdateDestroyAPIView.as_view(),
        name='user_update_destroy'
    )
]