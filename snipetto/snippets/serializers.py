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
            'name'  # we will not allow to edit or delete tag created once;
        )


class SnippetTagSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=64)


class ShortUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = (
            'id',
            'username',
        )


class SnippetSerializer(AuthorSerializerMixin, serializers.ModelSerializer):
    tags = SnippetTagSerializer(many=True)
    author = ShortUserSerializer(read_only=True)
    snippet = serializers.CharField(trim_whitespace=False)

    class Meta:
        model = Snippet
        fields = (
            'id',
            'created_at',
            'updated_at',
            'tags',
            'slug',
            'snippet',
            'author',
            'description'
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

    def update(self, instance, validated_data):
        tags = validated_data.pop('tags', None)
        if not tags:
            return super().update(instance, validated_data)
        tags_instances = []
        for tag in tags:
            tag_instance = Tag.objects.get_or_create(name=tag['name'])
            tags_instances.append(tag_instance[0])
        snippet = super().update(instance, validated_data)
        snippet.tags.clear()
        snippet.tags.add(*tags_instances)
        return snippet
