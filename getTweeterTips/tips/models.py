from django.db import models
from uuid import uuid4

# Create your models here.

class Tip(models.Model):
    """Model class to create the tips table"""
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )
    tweeted_at = models.DateTimeField(null=True, blank=True)
    python_tip = models.TextField()
    link = models.URLField(max_length=250)
    likes = models.PositiveIntegerField(null=True, blank=True)
    retweets = models.PositiveIntegerField(null=True, blank=True)
    who_posted = models.CharField(max_length=200)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'tips'

    def __str__(self):
        return self.python_tip
  