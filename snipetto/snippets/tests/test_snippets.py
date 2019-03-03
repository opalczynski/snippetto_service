from rest_framework import status
from rest_framework.reverse import reverse

from snipetto.core.base_tests import SnipettoTestCase
from snipetto.snippets.models import Snippet, Tag


class SnippetViewSetTestCase(SnipettoTestCase):

    def setUp(self):
        super().setUp()
        self.snippet = Snippet.objects.create(
            slug='myslug',
            author=self.user,
            snippet='mysnippet'
        )
        self.snippet.tags.add(Tag.objects.create(name='django'))
        self.the_other_snippet = Snippet.objects.create(
            slug='totallydifferentslug',
            author=self.user,
            snippet='mysnippet'
        )
        self.urls = {
            'list': reverse('v1:snippets-list'),
            'detail': reverse('v1:snippets-detail', args=(self.snippet.id, ))
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
            data={
                'slug': 'myslug2',
                'tags': [{'name': 'sometag'}],
                'snippet': 'def somefunc()',
            },
            **self.get_credentials()
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_destroy(self):
        response = self.client.delete(
            self.urls['detail'],
            **self.get_credentials()
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_edit(self):
        response = self.client.put(
            self.urls['detail'],
            data={
                'slug': 'newslug',
                # note here: on edit we exchange tag - remove old, add new
                'tags': [{'name': 'yetanothertag'}],
                'snippet': 'def somefunc()',
                'description': 'some desc',
            },
            **self.get_credentials()
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_filters(self):
        response = self.client.get(
            self.urls['list'],
            data={
                'slug': self.snippet.slug
            },
            **self.get_credentials()
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

        response = self.client.get(
            self.urls['list'],
            data={
                'tags': 'django'
            },
            **self.get_credentials()
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
