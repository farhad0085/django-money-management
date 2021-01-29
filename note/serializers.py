from rest_framework import serializers
from .models import Note
from tag.serializers import TagSerializer

class NoteSerializer(serializers.ModelSerializer):
    """Serializer for notes"""

    tags = TagSerializer(many=True)
    class Meta:
        model = Note
        fields = '__all__'