from django.urls import re_path
from . import views

urlpatterns = [
    re_path(
        r'^$',
        views.MessageCreateAPIView.as_view(),
        name='chat_messages_list'
    ),
    re_path(
        r'^(?P<pk>[^/]+)/?$',
        views.MessageDestroyAPIView.as_view(),
        name='message_destroy'
    ),
]