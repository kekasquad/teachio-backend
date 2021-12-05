from django.urls import re_path
from . import views

urlpatterns = [
    re_path(
        r'^user/?$',
        views.ChatListAPIView.as_view(),
        name='user_chats_list'
    ),
    re_path(
        r'^$',
        views.ChatCreateAPIView.as_view(),
        name='chat_create'
    ),
    re_path(
        r'^user/(?P<user_id>[^/]+)/?$',
        views.ChatWithUserAPIView.as_view(),
        name='chat_with_user'
    ),
    re_path(
        r'^(?P<chat_id>[^/]+)/messages/?$',
        views.ChatMessagesAPIView.as_view(),
        name='chat_messages_destroy'
    ),
    re_path(
        r'^(?P<pk>[^/]+)/?$',
        views.ChatDestroyAPIView.as_view(),
        name='chat_destroy'
    ),
]
