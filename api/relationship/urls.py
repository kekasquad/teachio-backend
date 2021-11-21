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
        views.RelationshipListCreateAPIView.as_view(),
        name='relationship_list_create'
    ),
    re_path(
        r'^(?P<pk>[^/]+)/?$',
        views.RelationshipRetrieveDestroyAPIView.as_view(),
        name='relationship_destroy'
    ),
]