from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4


class Entity(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=256)
    metadata = models.JSONField(null=True, blank=True)

class UserProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    fullname = models.CharField(max_length=256, null=True, blank=True)
    admin = models.BooleanField(default=False)
    entity = models.ForeignKey(Entity, related_name="user_profiles", null=True, blank=True, on_delete=models.SET_NULL)


