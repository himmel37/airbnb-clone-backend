from rest_framework import serializers
from users.serializers import TinyUserSerializer
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    user = TinyUserSerializer()

    class Meta:
        model = Review
        fields = (
            "user",
            "payload",
            "rating",
        )
