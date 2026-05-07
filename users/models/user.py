from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    ROLE_CHOICES = [
        ('ADMIN', 'Admin'),
        ('DEVELOPER', 'Developer'),
        ('TESTER', 'Tester'),
    ]

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='TESTER'
    )

    def __str__(self):
        return self.username