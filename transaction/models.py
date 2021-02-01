from django.db import models
from common.models import TrackingModel
from django.contrib.auth.models import User
from common.currencies import CURRENCIES

class Transaction(TrackingModel):
    """Model for transactions"""

    TRANSACTION_TYPES = [
        (0, "Earn"),
        (1, "Spend")
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="transactions")
    amount = models.FloatField()
    title = models.CharField(max_length=200)
    body = models.TextField(blank=True)
    transaction_type = models.IntegerField(choices=TRANSACTION_TYPES)
    currency = models.CharField(max_length=20, choices=CURRENCIES, default='USD', blank=True)
    tags = models.ManyToManyField("tag.Tag", related_name="transactions")

    def __str__(self):
        return self.user.username
