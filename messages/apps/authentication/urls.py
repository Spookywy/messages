from django.urls import path
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
)


from . import views
from . import forms


urlpatterns = [
    path(
        "",
        LoginView.as_view(
            template_name="authentication/login.html",
            redirect_authenticated_user=True,
            authentication_form=forms.UserLoginForm,
        ),
        name="login",
    ),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
]
