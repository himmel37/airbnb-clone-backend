from django.db import models
from common.models import CommonModel


class Wishlist(CommonModel):
    """Wish list Model Definition"""

    name = models.CharField(
        max_length=180,
    )
    rooms = models.ManyToManyField(
        "rooms.Room",
    )
    experiences = models.ManyToManyField(
        "experiences.Experience",
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name
