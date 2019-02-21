from rest_framework import serializers

from snipetto.authentication.models import UserToken


class TokenReadOnlySerializer(serializers.ModelSerializer):

    class Meta:
        model = UserToken
        fields = (
            'key',
        )
        read_only_fields = (
            'key',
        )


class InitSerializer(serializers.Serializer):
    username = serializers.SlugField()
    password = serializers.CharField(max_length=256, min_length=8)
