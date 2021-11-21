from django.urls import re_path
from . import views

urlpatterns = [
    re_path(
        r'^user/?$',
        views.NoteListAPIView.as_view(),
        name='user_notes_list'
    ),
    re_path(
        r'^$',
        views.NoteListCreateAPIView.as_view(),
        name='note_list_create'
    ),
    re_path(
        r'^(?P<pk>[^/]+)/?$',
        views.NoteRetrieveUpdateDestroyAPIView.as_view(),
        name='note_retrieve_update_destroy'
    ),
]
