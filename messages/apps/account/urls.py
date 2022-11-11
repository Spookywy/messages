from django.urls import path
from django.contrib.auth.views import (
    PasswordChangeView,
    PasswordChangeDoneView,
)

from . import views


urlpatterns = [
    path("", views.AccountView.as_view(), name="account"),
    path("change-password/", PasswordChangeView.as_view(), name="change_password"),
    path(
        "password-change-done/",
        PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
]
