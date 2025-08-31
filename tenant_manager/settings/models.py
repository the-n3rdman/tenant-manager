from django.db import models
from uuid import uuid4
from authentication.models import Entity, User, UserProfile
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
import os
from django.utils import timezone
# Create your models here.


class Location(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=256)
    entity = models.ForeignKey(Entity, related_name="locations", on_delete=models.CASCADE)
    metadata = models.JSONField(null=True, blank=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Building(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=256)
    entity = models.ForeignKey(Entity, related_name="buildings", on_delete=models.CASCADE)
    location = models.ForeignKey(Location, related_name="buildings", on_delete=models.CASCADE)
    metadata = models.JSONField(null=True, blank=True)
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name


class Floor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=256)
    entity = models.ForeignKey(Entity, related_name="floors", on_delete=models.CASCADE)
    building = models.ForeignKey(Building, related_name="floors", on_delete=models.CASCADE)
    metadata = models.JSONField(null=True, blank=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Room(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=256)
    entity = models.ForeignKey(Entity, related_name="rooms", on_delete=models.CASCADE)
    floor = models.ForeignKey(Floor, related_name="rooms", on_delete=models.CASCADE)
    metadata = models.JSONField(null=True, blank=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Bed(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=256)
    entity = models.ForeignKey(Entity, related_name="beds", on_delete=models.CASCADE)
    room = models.ForeignKey(Room, related_name="beds", on_delete=models.CASCADE)
    metadata = models.JSONField(null=True, blank=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Amenity(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=256)
    identifier = models.CharField(max_length=256, null=True, blank=True)
    entity = models.ForeignKey(Entity, related_name="amentities", on_delete=models.CASCADE)
    metadata = models.JSONField(null=True, blank=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name + self.identifier if self.identifier else self.name 


class AmenityDeploymentMap(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    deployment_date = models.DateTimeField(null=True, blank=True)
    metadata = models.JSONField(null=True, blank=True)
    status = models.BooleanField(default=True)
    amenity = models.ForeignKey(Amenity, related_name="amenity_deployment_map", on_delete=models.CASCADE)
    # Mapping a model to multiple models directly 
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.UUIDField()
    deployed_to = GenericForeignKey("content_type", "object_id")



class Tenant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=256)
    entity = models.ForeignKey(Entity, related_name="tenants", on_delete=models.CASCADE)
    phone = models.CharField(max_length=256, null=True, blank=True)
    uidai = models.CharField(max_length=256, null=True, blank=True)
    metadata = models.JSONField(null=True, blank=True)
    status = models.BooleanField(default=True)
    bed = models.ForeignKey(Bed, related_name="tenants", on_delete=models.CASCADE)
    date_of_joining = models.DateTimeField(null=True, blank=True)
    shifting_history = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.name


class PaymentHistory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    tenant = models.ForeignKey(Tenant, related_name="payment_history", on_delete=models.CASCADE)
    payment_date = models.DateTimeField(null=True, blank=True)
    paid_amount = models.FloatField(null=True, blank=True)
    due_amount = models.FloatField(null=True, blank=True)
    metadata = models.JSONField(null=True, blank=True)
    status = models.BooleanField(default=True)


def upload_with_datetime(instance, filename):
    base, ext = os.path.splitext(filename)
    timestamp = timezone.now().strftime("%Y%m%d_%H%M%S")
    return f"documents/{base}_{timestamp}{ext}"

class Document(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to=upload_with_datetime)   # will store under MEDIA_ROOT/documents/
    uploaded_at = models.DateTimeField(auto_now_add=True)


class TenantDocumentMap(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    tenant = models.ForeignKey(Tenant, related_name="tenant_document_map", on_delete=models.CASCADE)
    document = models.ForeignKey(Document, related_name="tenant_document_map", on_delete=models.CASCADE)
    name = models.CharField(max_length=256, null=True, blank=True)
    metadata = models.JSONField(null=True, blank=True)
    status = models.BooleanField(default=True)


class TenantAmenityMap(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    tenant = models.ForeignKey(Tenant, related_name="tenant_amenity_map", on_delete=models.CASCADE)
    amenity = models.ForeignKey(Amenity, related_name="tenant_amenity_map", on_delete=models.CASCADE)
    metadata = models.JSONField(null=True, blank=True)
    status = models.BooleanField(default=True)

