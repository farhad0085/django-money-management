from .serializers import TagSerializer
from .models import Tag
from rest_framework.viewsets import ModelViewSet


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def get_serializer(self, *args, **kwargs):
        """ if an array is passed, set serializer to many """
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many'] = True
        return super(TagViewSet, self).get_serializer(*args, **kwargs)