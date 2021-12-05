from django.urls import re_path
from . import views

urlpatterns = [
    re_path(
        r'^(?P<student_id>[^/]+)/?$',
        views.StudentNoteRetrieveUpdateAPIView.as_view(),
        name='teacher_students_note_retrieve_update'
    ),
]