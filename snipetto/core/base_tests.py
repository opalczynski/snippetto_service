from django.contrib.auth.models import User
from django.test import TestCase

from rest_framework.reverse import reverse
from rest_framework.test import APIClient


class SnipettoTestCase(TestCase):

    def setUp(self):
        super().setUp()
        self.client = APIClient()
        self.user = User.objects.create(username='user',
                                        email='user@example.com')
        self.user.set_password('pass4321')
        self.user.save()

    def get_credentials(self):
        response = self.client.post(
            reverse('v1:user-init'),
            data={
                'username': 'user',
                'password': 'pass4321'
            }
        )

        return {
            'HTTP_AUTHORIZATION': 'Token {}'.format(response.data['key'])
        }
