"""Serializer"""

from rest_framework import serializers, fields
from rest_framework.validators import UniqueValidator
from .models import Tip


class TipSerializer(serializers.ModelSerializer):
    tweeted_at = fields.DateTimeField(input_formats=['%Y-%m-%dT%H:%M:%SZ'])
    python_tip = fields.CharField(max_length=140)
    class Meta:
        model = Tip
        fields = ("id", "tweeted_at", "python_tip", "link",
                    "likes", "retweets", "who_posted", "published")
        read_only_fields = "id",
