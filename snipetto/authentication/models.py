import uuid
from hashlib import sha256

from django.contrib.auth import get_user_model
from django.db import models


def get_token():
    return sha256(uuid.uuid4().hex.encode()).hexdigest()


class UserToken(models.Model):
    """It is dumb simple long living token model - we do not care 
    much about security now;"""""

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    key = models.CharField(max_length=64, default=get_token)
