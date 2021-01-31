from django.urls import path
from .views import *

urlpatterns = [
    path('login/', LoginView.as_view(), name="auth_login"),
    path('logout/', LogoutView.as_view(), name="auth_logout"),
    path('user/me/', UserInfo.as_view(), name="auth_user_info"),
    path('register/', RegistrationView.as_view(), name="auth_register"),
]
