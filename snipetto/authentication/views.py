from django.contrib.auth.models import User

from rest_framework import views
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from snipetto.authentication.models import UserToken
from snipetto.authentication.serializers import (
    InitSerializer,
    TokenReadOnlySerializer
)


class InitializeUserView(views.APIView):
    authentication_classes = ()
    permission_classes = ()

    def post(self, request, *args, **kwargs):
        # dummy get or create user view

        init_serializer = InitSerializer(data=request.data)
        init_serializer.is_valid(raise_exception=True)

        username = init_serializer.validated_data['username']
        password = init_serializer.validated_data['password']

        try:
            user, created = User.objects.get(username=username), False
        except User.DoesNotExist:
            # django requires email - to lazy to change that;
            # and thus get_or_create will fail;
            user, created = User.objects.create(
                username=username,
                is_active=True,
                email="{}@fake.com".format(username)
            ), True

        if created:
            user.set_password(password)
            user.save()
        else:
            if not user.check_password(password):
                raise ValidationError("Wrong password")

        token, _ = UserToken.objects.get_or_create(user=user)

        return Response(
            data=TokenReadOnlySerializer(instance=token).data
        )
