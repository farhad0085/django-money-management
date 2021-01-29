from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TransactionData, TransactionViewSet

router = DefaultRouter()
router.register("", TransactionViewSet)

urlpatterns = [
    path("data/", TransactionData.as_view()),
    path("", include(router.urls)),
]