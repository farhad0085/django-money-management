from rest_framework import serializers
from .models import Tag

class TagSerializer(serializers.ModelSerializer):
    """Serializer for tags"""

    class Meta:
        model = Tag
        fields = '__all__'