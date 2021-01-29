from .serializers import NoteSerializer
from .models import Note
from rest_framework.viewsets import ModelViewSet


class NoteViewSet(ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer