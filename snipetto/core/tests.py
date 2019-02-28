from rest_framework import status
from rest_framework.reverse import reverse

from snipetto.core.base_tests import SnipettoTestCase


class UrlsMappingTestCase(SnipettoTestCase):

    def setUp(self):
        super().setUp()
        self.url = reverse('v1:api-paths')

    def test_paths(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('tags', response.data)
        self.assertIn('snippets', response.data)
        self.assertIn('auth', response.data)
        self.assertIn('list', response.data['tags'])
        self.assertIn('list', response.data['snippets'])
        self.assertIn('init', response.data['auth'])
