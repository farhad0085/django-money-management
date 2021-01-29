from rest_framework import serializers
from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    """Serializer for notes"""

    class Meta:
        model = Note
        fields = '__all__'

    def create(self, validated_data):

        note = Note.objects.create(
            user=self.context['request'].user,
            title=validated_data['title'],
            body=validated_data['body']
        )

        for tag in validated_data['tags']:
            note.tags.add(tag)
        return note

    