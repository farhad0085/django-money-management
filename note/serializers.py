from rest_framework import serializers
from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    """Serializer for notes"""

    class Meta:
        model = Note
        fields = '__all__'
        read_only_fields = ["user"]

    def create(self, validated_data):

        note = Note.objects.create(
            user=self.context['request'].user,
            title=validated_data.get('title'),
            body=validated_data.get('body', validated_data.get('title'))
        )

        for tag in validated_data.get('tags', []):
            note.tags.add(tag)
        return note

    