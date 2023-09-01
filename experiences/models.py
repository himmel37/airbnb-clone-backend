from django.db import models
from common.models import CommonModel


class Experience(CommonModel):
    """Experience Model Definition"""

    country = models.CharField(
        max_length=50,
        default="한국",
    )
    city = models.CharField(
        max_length=80,
        default="서울",
    )
    name = models.CharField(
        max_length=180,
        default="",
    )
    price = models.PositiveIntegerField()
    host = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="experiences",
    )
    description = models.TextField()
    address = models.CharField(
        max_length=250,
    )
    start = models.TimeField()
    end = models.TimeField()
    perks = models.ManyToManyField(
        "experiences.Perk",
    )
    category = models.ForeignKey(
        "categories.Category",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="experiences",
    )

    def __str__(self):
        return self.name


class Perk(CommonModel):
    """Perk Definition"""

    name = models.CharField(
        max_length=150,
    )
    detail = models.CharField(
        max_length=250,
        blank=True,
        default="",
    )
    explain = models.TextField(
        blank=True,
        default="",
    )

    def __str__(self):
        return self.name
