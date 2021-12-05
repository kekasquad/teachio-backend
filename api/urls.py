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
    re_path(r'^lesson/', include('api.lesson.urls')),
    re_path(r'^chat/', include('api.chat.urls')),
    re_path(r'^relationship/', include('api.relationship.urls')),
    re_path(r'^user/', include('api.user.urls')),
    re_path(r'^message/', include('api.message.urls')),
    re_path(r'^finance/', include('api.finance.urls')),
    re_path(r'^student_note/', include('api.student_note.urls')),
    re_path(
        r'^swagger/$',
        schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'
    ),
]
