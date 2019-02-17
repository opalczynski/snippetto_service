from django.db.models import Q

from django_filters import rest_framework as filters

from snipetto.snippets.models import Snippet


class SnippetFilter(filters.FilterSet):
    slug = filters.CharFilter(lookup_expr='icontains')
    tags = filters.CharFilter(method='filter_tags')

    class Meta:
        model = Snippet
        fields = (
            'slug',
            'tags'
        )

    def filter_tags(self, queryset, name, value):
        q_filters = Q()
        if value:
            for tag_name in value.split(','):
                q_filters |= Q(tags__name=tag_name.strip(), _connector=Q.OR)
            queryset = queryset.filter(q_filters)
            return queryset.distinct()
        return queryset
