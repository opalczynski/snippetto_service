from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.reverse import reverse

from snipetto.core.base_tests import SnipettoTestCase


class InitializeUserTestCase(SnipettoTestCase):

    def setUp(self):
        super().setUp()
        self.url = reverse('v1:user-init')

    def _base_test(self):
        response = self.client.post(
            self.url,
            data={
                'username': 'hiho',
                'password': 'test1234'
            }
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # one is exsiting in base test class
        self.assertEqual(User.objects.count(), 2)

    def _create_test_user(self):
        user = User.objects.create(email='dummy@example.com', username='hiho')
        user.set_password('test1234')
        user.save()

    def test_initialization_when_user_does_not_exist(self):
        self._base_test()

    def test_initialization_when_user_exists(self):
        self._create_test_user()
        self._base_test()

    def test_bad_password_for_existing_user(self):
        self._create_test_user()
        response = self.client.post(
            self.url,
            data={
                'username': 'hiho',
                'password': 'test1235'
            }
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
