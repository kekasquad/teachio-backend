from django.urls import re_path, include

urlpatterns = [
    re_path(r'^auth/', include('api.auth.urls')),
    re_path(r'^notification/', include('api.notification.urls')),
    re_path(r'^stats/', include('api.stats.urls')),
]
