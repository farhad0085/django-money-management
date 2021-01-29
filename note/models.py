from django.contrib.auth.models import User
from django.db import models
from common.models import TrackingModel
from money.models import Tag


class Note(TrackingModel):
    """Model for notes"""

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")
    title = models.CharField(max_length=500, blank=True, null=True)
    body = models.TextField(blank=True)
    tags = models.ManyToManyField(Tag, related_name="notes")

    def __str__(self):
        return self.title
