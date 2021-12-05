from django.urls import re_path
from . import views

urlpatterns = [
    re_path(
        r'^user/?$',
        views.RelationshipListAPIView.as_view(),
        name='user_relationship_list'
    ),
    re_path(
        r'^$',
        views.RelationshipCreateAPIView.as_view(),
        name='relationship_list_create'
    ),
    re_path(
        r'^link/?$',
        views.RelationshipLinkAPIView.as_view(),
        name='relationship_link'
    ),
    re_path(
        r'^(?P<teacher_id>[^/]+)/(?P<student_id>[^/]+)/?$',
        views.RelationshipRetrieveDestroyAPIView.as_view(),
        name='relationship_retrieve_destroy'
    ),
]