from django.urls import re_path
from . import views

urlpatterns = [
    re_path(
        r'^$',
        views.LessonListCreateAPIView.as_view(),
        name='lesson_list_create'
    ),
    re_path(
        r'^(?P<pk>[^/]+)/?$',
        views.LessonRetrieveUpdateDestroyAPIView.as_view(),
        name='lesson_retrieve_update_destroy'
    )
]