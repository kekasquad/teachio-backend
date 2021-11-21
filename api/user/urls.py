from django.urls import re_path
from . import views

urlpatterns = [
    re_path(
        r'^$',
        views.CurrentUserAPIView.as_view(),
        name='user_list'
    ),
    re_path(
        r'^(?P<pk>[^/]+)/?$',
        views.UserRetrieveUpdateDestroyAPIView.as_view(),
        name='user_update_destroy'
    )
]