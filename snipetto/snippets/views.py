from rest_framework import mixins, viewsets
from rest_framework.viewsets import GenericViewSet

from django_filters.rest_framework import DjangoFilterBackend
from snipetto.snippets.filters import SnippetFilter
from snipetto.snippets.models import Snippet, Tag
from snipetto.snippets.serializers import SnippetSerializer, TagSerializer


class TagViewSet(mixins.CreateModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.ListModelMixin,
                 GenericViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class SnippetViewSet(viewsets.ModelViewSet):
    serializer_class = SnippetSerializer

    filter_backends = (DjangoFilterBackend, )
    filter_class = SnippetFilter

    def get_queryset(self):
        return Snippet.objects.filter(author=self.request.user).all()
