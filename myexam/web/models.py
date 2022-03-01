from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

USERNAME_EXCEPTION_MSG = "Ensure this value contains only letters, numbers, and underscore."


def validate_username(value):
    for v in value:
        if v.isalnum() or v == '_':
            continue
        else:
            raise ValidationError(USERNAME_EXCEPTION_MSG)


class Profile(models.Model):
    NAME_MIN_LEN = 2
    NAME_MAX_LEN = 15

    AGE_MIN_VALUE = 0

    Username = models.CharField(
        max_length=NAME_MAX_LEN,
        validators=(
            MinLengthValidator(NAME_MIN_LEN),
            validate_username,
        ),
    )

    Email = models.EmailField()

    Age = models.IntegerField(
        null=True,
        blank=True,
        validators=(
            MinValueValidator(AGE_MIN_VALUE),
        )
    )


class Album(models.Model):
    MAX_LENGTH = 30
    PRICE_MIN_VALUE = 0
    CHOICES = [("Pop Music", "Pop Music"),
               ("Jazz Music", "Jazz Music"),
               ("R&B Music", "R&B Music"),
               ("Rock Music", "Rock Music"),
               ("Country Music", "Country Music"),
               ("Dance Music", "Dance Music"),
               ("Hip Hop Music", "Hip Hop Music"),
               ("Other", "Other")]

    Album_Name = models.CharField(
        max_length=MAX_LENGTH,
        unique=True,
    )

    Artist = models.CharField(
        max_length=MAX_LENGTH,
    )

    Genre = models.CharField(
        max_length=MAX_LENGTH,
        choices=CHOICES,
    )

    Description = models.TextField(
        null=True,
        blank=True,
    )

    Image_URL = models.URLField()

    Price = models.FloatField(
        validators=(
            MinValueValidator(PRICE_MIN_VALUE),
        )
    )

    class Meta:
        ordering = ('Album_Name',)