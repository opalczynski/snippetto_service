from django.urls import reverse

from rest_framework.response import Response
from rest_framework.views import APIView


class UrlsMappingAPIView(APIView):
    def get(self, request):
        url_mapping = {
            'tags': {
                'list': reverse('v1:tags-list'),
            },
            'snippets': {
                'list': reverse('v1:tags-list'),
                'detail': reverse('v1:tags-detail')
            },
            'auth': {
                'login': ''
            }
        }
        return Response(url_mapping)
