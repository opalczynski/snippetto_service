from django.contrib.auth import get_user_model

from rest_framework import serializers

from snipetto.core.serializers import AuthorSerializerMixin
from snipetto.snippets.models import Snippet, Tag


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = (
            'id',
            'created_at',
            'updated_at',
            'name'
        )
        read_only_fields = (
            'id',
            'created_at',
            'updated_at',
            'name'  # we will not allow to edit tag created once;
        )


class GetOrCreateTagSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=64)


class ShortUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = (
            'id',
            'username',
            'email',
        )


class SnippetSerializer(AuthorSerializerMixin, serializers.ModelSerializer):
    tags = GetOrCreateTagSerializer(many=True)
    author = ShortUserSerializer(read_only=True)

    class Meta:
        model = Snippet
        fields = (
            'id',
            'created_at',
            'updated_at',
            'tags',
            'slug',
            'snippet',
            'author'
        )
        read_only_fields = (
            'id',
            'created_at',
            'updated_at',
            'author',
        )

    def create(self, validated_data):
        tags = validated_data.pop('tags')
        tags_instances = []
        for tag in tags:
            tag_instance = Tag.objects.get_or_create(name=tag['name'])
            tags_instances.append(tag_instance[0])
        snippet = super().create(validated_data)
        snippet.tags.add(*tags_instances)
        return snippet
