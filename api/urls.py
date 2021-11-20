from rest_framework import permissions
from django.urls import re_path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="API docs",
      default_version='v1',
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    re_path(r'^auth/', include('api.auth.urls')),
    re_path(r'^notification/', include('api.notification.urls')),
    re_path(r'^stats/', include('api.stats.urls')),
    re_path(r'^note/', include('api.note.urls')),
    re_path(
        r'^swagger/$',
        schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'
    ),
]
