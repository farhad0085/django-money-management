from django.db import models
from common.models import TrackingModel

class Tag(TrackingModel):
    """Model for tags"""

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
