from django.urls import path, include
from rest_auth.views import PasswordResetConfirmView
from .views import (
    LoginView,
    RegistrationView,
    UserInfo,
)


urlpatterns = [
    path('login/', LoginView.as_view()),
    path('user/me/', UserInfo.as_view()),
    path('password/reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('register/', RegistrationView.as_view()),
    path('register/', include('rest_auth.registration.urls')),
    path('', include('rest_auth.urls')),
]
