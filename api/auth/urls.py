from django.urls import re_path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)
from . import views

urlpatterns = [
    re_path(
        r'^token/?$',
        TokenObtainPairView.as_view(),
        name='auth_token_obtain_pair'
    ),
    re_path(
        r'^token/refresh/?$',
        TokenRefreshView.as_view(),
        name='auth_token_refresh'
    ),
    re_path(
        r'^signup/?',
        views.SignUpAPIView.as_view(),
        name='auth_signup'
    )
]
