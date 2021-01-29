from django.contrib.auth.models import User
from django.db import models
from common.models import TrackingModel

class Tag(TrackingModel):
    """Model for tags"""

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_tags")
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
