from django.urls import re_path
from . import views

urlpatterns = [
    re_path(
        r'^$',
        views.ChatListCreateAPIView.as_view(),
        name='chat_list_create'
    ),
    re_path(
        r'^(?P<pk>[^/]+)/?$',
        views.ChatRetrieveUpdateDestroyAPIView.as_view(),
        name='chat_retrieve_update_destroy'
    ),
    re_path(
        r'^user/?$',
        views.ChatListAPIView.as_view(),
        name='user_chats_list'
    )
]