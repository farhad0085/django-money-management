from django.db import models
from common.models import TrackingModel
from django.contrib.auth.models import User


class Transaction(TrackingModel):
    """Model for transactions"""

    transaction_types = [
        (0, "Earn"),
        (1, "Spend")
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="transactions")
    amount = models.FloatField()
    title = models.CharField(max_length=200)
    body = models.TextField(blank=True)
    transaction_type = models.IntegerField(choices=transaction_types)
    tags = models.ManyToManyField("tag.Tag", related_name="transactions")

    def __str__(self):
        return self.user.username
