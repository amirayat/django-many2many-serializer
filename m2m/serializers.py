from rest_framework import serializers
from rest_framework.exceptions import NotFound
from m2m.models import *


class TagSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=True)
    class Meta:
        model = Tag
        fields = '__all__'


class PostSerializer(serializers.HyperlinkedModelSerializer):
    tag = TagSerializer(read_only=True, many=True)

    class Meta:
        model = Post
        fields = '__all__'


class PostModelSerializer(serializers.HyperlinkedModelSerializer):
    tag = TagSerializer(read_only=True, many=True)

    class Meta:
        model = Post
        fields = '__all__'


class PostHyperlinkedSerializer(serializers.HyperlinkedModelSerializer):
    tag = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='tag-detail'
    )

    class Meta:
        model = Post
        fields = '__all__'


class WritablePostSerializer(serializers.HyperlinkedModelSerializer):
    tag = TagSerializer(many = True)

    class Meta:
        model = Post
        fields = '__all__'

    def unpack(self, s: set):
        return ",".join(map(str, s))

    def create(self, validated_data):
        entered_tags = validated_data.pop('tag')
        entered_tags_id = set([tag.get("id") for tag in entered_tags])
        exist_tags_id = set(Tag.objects.filter(id__in = entered_tags_id).values_list('id', flat=True))
        dif = entered_tags_id - exist_tags_id
        if dif:
            raise NotFound(f'{self.unpack(dif)} tag not found!')
        post = Post.objects.create(**validated_data)
        post.tag.set(list(entered_tags_id))
        return post

    def update(self, instance, validated_data):
        ...
        return super().update(instance, validated_data)