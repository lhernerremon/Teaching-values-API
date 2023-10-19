from django.contrib.auth.models import AbstractUser
from django.db import models
from model_utils.models import TimeStampedModel


class User(AbstractUser, TimeStampedModel):
    name = models.CharField("nombre", blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore
