from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, viewsets
from rest_framework.viewsets import GenericViewSet

from snipetto.snippets.filters import SnippetFilter
from snipetto.snippets.models import Tag, Snippet
from snipetto.snippets.serializers import TagSerializer, SnippetSerializer


class TagViewSet(mixins.CreateModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.DestroyModelMixin,
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
