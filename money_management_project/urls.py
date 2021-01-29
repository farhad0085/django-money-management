from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from common.logger_utils import *

schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="API documentation for money management project",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="farhadhossain0085@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # documentation
    path("api/documentation/swagger/", schema_view.with_ui('swagger', cache_timeout=0)),
    path("api/documentation/", schema_view.with_ui('redoc', cache_timeout=0)),

    path('admin/', admin.site.urls),
    path('api/auth/', include("user.urls")),
    path('api/note/', include('note.urls')),
]
