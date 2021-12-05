from django.urls import re_path
from . import views

urlpatterns = [
    re_path(
        r'^user/?$',
        views.FinanceListAPIView.as_view(),
        name='user_finance_list'
    )
]