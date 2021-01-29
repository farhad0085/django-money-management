from transaction.validators import DateRangeValidator
from transaction.models import Transaction
from rest_framework import serializers
from tag.models import Tag

class TransactionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Transaction
        fields = "__all__"
        read_only_fields = ["user"]

    def create(self, validated_data):

        transaction = Transaction.objects.create(
            user=self.context['request'].user,
            title=validated_data.get('title'),
            body=validated_data.get('body', validated_data.get('title')),
            amount=validated_data.get("amount"),
            transaction_type=validated_data.get("transaction_type")
        )

        for tag in validated_data.get('tags', []):
            transaction.tags.add(tag)
        return transaction


class DateRangeSerializer(serializers.Serializer):
    date_from = serializers.DateField()
    date_to = serializers.DateField()

    class Meta:
        validators = [DateRangeValidator]