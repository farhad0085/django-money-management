from django.urls import path, include
from .views import (
    LoginView,
    RegistrationView,
    UserInfo,
)

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('user/me/', UserInfo.as_view()),
    path('register/', RegistrationView.as_view()),
]
