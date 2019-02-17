from rest_framework.authentication import TokenAuthentication

from snipetto.authentication.models import UserToken


class DumbTokenAuthentication(TokenAuthentication):
    model = UserToken
