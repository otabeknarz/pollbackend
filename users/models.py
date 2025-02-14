from django.db import models
from django.contrib.auth.models import AbstractUser
import random


def get_random_id() -> str:
    return str(random.randint(1000000000, 9999999999))


class User(AbstractUser):
    class PollChoices(models.TextChoices):
        TOSHKENT = "TOSHKENT", "Toshkent"
        SAMARQAND = "SAMARQAND", "Samarqand"
        BUXORO = "BUXORO", "Buxoro"
        ANDIJON = "ANDIJON", "Andijon"
        SIRDARYO = "SIRDARYO", "Sirdaryo"

    id = models.CharField(
        max_length=40,
        primary_key=True,
        unique=True,
        null=False,
        blank=False,
        default=get_random_id,
    )
    email = models.EmailField(null=True, blank=True)
    choice = models.CharField(
        max_length=20, choices=PollChoices.choices, null=True, blank=True
    )

    def __str__(self):
        return f"{self.id} - {self.first_name} {self.last_name}"
