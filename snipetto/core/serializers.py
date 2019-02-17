

class AuthorSerializerMixin:

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)
