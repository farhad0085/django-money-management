from rest_framework import serializers
from .models import Note
from tag.serializers import TagSerializer
from tag.models import Tag


class NoteSerializer(serializers.ModelSerializer):
    """Serializer for notes"""
    
    tags = TagSerializer(many=True)

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

        for tag in validated_data.get('tags'):
            # check if tag exists or not
            _tag = Tag.objects.filter(name=tag['name'], created_by=self.context['request'].user).first()
            
            # if tag not exist, create one
            if not _tag:
                _tag = Tag.objects.create(name=tag['name'], created_by=self.context['request'].user)
            
            # now attach it with the transaction
            note.tags.add(_tag)

        return note

    