from transaction.validators import DateRangeValidator
from transaction.models import Transaction
from rest_framework import serializers
from tag.models import Tag
from tag.serializers import TagSerializer


class TransactionSerializer(serializers.ModelSerializer):

    tags = TagSerializer(many=True)

    class Meta:
        model = Transaction
        fields = "__all__"
        read_only_fields = ["user"]

    def create(self, validated_data):
        
        user = self.context['request'].user

        transaction = Transaction.objects.create(
            user=user,
            title=validated_data.get('title'),
            body=validated_data.get('body', validated_data.get('title')),
            amount=validated_data.get("amount"),
            transaction_type=validated_data.get("transaction_type"),
            currency=validated_data.get("currency", user.user_profile.currency)
        )

        for tag in validated_data.get('tags'):

            # check if tag exists or not
            _tag = Tag.objects.filter(name=tag['name'], created_by=self.context['request'].user).first()
            
            # if tag not exist, create one
            if not _tag:
                _tag = Tag.objects.create(name=tag['name'], created_by=self.context['request'].user)
            
            # now attach it with the transaction
            transaction.tags.add(_tag)
        return transaction


class DateRangeSerializer(serializers.Serializer):
    date_from = serializers.DateField()
    date_to = serializers.DateField()

    class Meta:
        validators = [DateRangeValidator]