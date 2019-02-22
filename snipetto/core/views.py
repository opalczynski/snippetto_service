from django.urls import reverse

from rest_framework.response import Response
from rest_framework.views import APIView


class UrlsMappingAPIView(APIView):
    authentication_classes = ()
    permission_classes = ()

    def get(self, request, *args, **kwargs):
        url_mapping = {
            'tags': {
                'list': reverse('v1:tags-list'),
            },
            'snippets': {
                'list': reverse('v1:snippets-list'),
            },
            'auth': {
                'init': reverse('v1:user-init')
            }
        }
        return Response(url_mapping)
