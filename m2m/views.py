from rest_framework.viewsets import ModelViewSet
from m2m.models import *
from m2m.serializers import *


class TagViewset(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class PostViewset(ModelViewSet):
    queryset = Post.objects.all()

    def get_serializer_class(self):
        serializer = self.request.query_params.get('serializer')
        if not serializer:
            return PostModelSerializer
        elif serializer == 'ModelSerializer':
            return PostModelSerializer
        elif serializer == 'HyperlinkedSerializer':
            return PostHyperlinkedSerializer
        elif serializer == 'Writable':
            return WritablePostSerializer