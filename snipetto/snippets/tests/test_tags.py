from rest_framework import status
from rest_framework.reverse import reverse

from snipetto.core.base_tests import SnipettoTestCase
from snipetto.snippets.models import Tag


class TagViewSetTestCase(SnipettoTestCase):

    def setUp(self):
        super().setUp()
        self.tag = Tag.objects.create(name='sampletag')
        self.urls = {
            'list': reverse('v1:tags-list'),
            'detail': reverse('v1:tags-detail', args=(self.tag.id, ))
        }

    def test_list(self):
        response = self.client.get(
            self.urls['list'],
            **self.get_credentials()
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail(self):
        response = self.client.get(
            self.urls['detail'],
            **self.get_credentials()
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create(self):
        response = self.client.post(
            self.urls['list'],
            data={'name': 'mytag'},
            **self.get_credentials()
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
