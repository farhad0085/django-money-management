from rest_framework import serializers
from .models import Tag

class TagSerializer(serializers.ModelSerializer):
    """Serializer for tags"""

    class Meta:
        model = Tag
        fields = '__all__'
        read_only_fields = ['created_by']

    def create(self, validated_data):
        # check if tag exists or not
        tag = Tag.objects.filter(name=validated_data['name'], created_by=self.context['request'].user).first()
        
        # if tag not exist, create one
        if not tag:
            tag = Tag.objects.create(name=validated_data['name'], created_by=self.context['request'].user)
        return tag