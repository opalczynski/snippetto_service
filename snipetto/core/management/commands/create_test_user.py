from django.contrib.auth.models import User
from django.core.management import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        user = User.objects.create(
            is_active=True,
            username='testuser',
            email='testuser@fake.com'
        )
        user.set_password('testpass1234')
        user.save()
        print('User created.')
