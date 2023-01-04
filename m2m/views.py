from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response

from m2m.models import Post, Tag
from m2m.serializers import *


class TagViewset(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class PostViewset(ModelViewSet):
    queryset = Post.objects.all()

    def get_serializer_class(self):
        serializer = self.request.query_params.get('serializer')
        if not serializer:
            return PostSerializer
        elif serializer == 'ModelSerializer':
            return PostModelSerializer
        elif serializer == 'HyperlinkedSerializer':
            return PostHyperlinkedSerializer
        elif serializer == 'Writable':
            return WritablePostSerializer


class AdelView(APIView):
    permission_classes = [permissions.AllowAny]
    
    def get(self, request, format=None):
        posts = Post.objects.all()
        serializer = MyPostSerializer(posts, many=True)
        # print(serializer)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        data = request.data
        # print('========================\n',data)
        serializer = MyPostSerializer(data=data)
        # print('here serializer:\n', serializer,'\n\n')
        if serializer.is_valid():
            print('validated')
            # serializer.save()
            print(serializer)
            # return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.data)
        else:
            print('not validate')
            return Response(serializer.errors)

    def patch(self, request, *args, **kwargs):
        entered_tags = validated_data.pop('tag')
        entered_tags_id = set([tag.get("id") for tag in entered_tags])
        exist_tags_id = set(Tag.objects.filter(id__in = entered_tags_id).values_list('id', flat=True))
        dif = entered_tags_id - exist_tags_id
        if dif:
            raise NotFound(f'{self.unpack(dif)} tag not found!')
        post = Post.objects.create(**validated_data)
        post.tag.set(list(entered_tags_id))
        return post

        userstrat = self.get_queryset()
        serializer = self.get_serializer(userstrat, many=True)
        return Response(serializer.data)