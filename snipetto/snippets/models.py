from django.contrib.auth import get_user_model
from django.db import models

from snipetto.core.models import TimestampAbstractModel


class Tag(TimestampAbstractModel):
    name = models.CharField(max_length=64, unique=True)


class Snippet(TimestampAbstractModel):
    slug = models.SlugField(max_length=128, unique=True)
    description = models.CharField(max_length=2048, null=True, blank=True)
    tags = models.ManyToManyField(to=Tag)
    snippet = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING)
