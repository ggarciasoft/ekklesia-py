from django.db import models
#from django.contrib.auth.models import User
from django_tenants.models import TenantMixin, DomainMixin
from django.contrib.auth.models import User

# Create your models here.
class Organization(TenantMixin):
    name = models.CharField(max_length=100)
    # default true, schema will be automatically created and synced when it is saved
    auto_create_schema = True
class Domain(DomainMixin):
    pass
class EntityType(models.Model):
    alias = models.CharField(max_length=20, blank=False, null=False)
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=255)
    is_active = models.BooleanField(null=False)
    insert_user = models.ForeignKey(User, related_name="entity_type_insert_user", on_delete=models.DO_NOTHING)
    insert_date = models.DateTimeField()
    update_user = models.ForeignKey(User, related_name="entity_type_update_user", null=True, on_delete=models.DO_NOTHING)
    update_date = models.DateTimeField(null=True)
    
class ActivityType(models.Model):
    alias = models.CharField(max_length=20, blank=False, null=False)
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=255)
    is_active = models.BooleanField(null=False)
    insert_user = models.ForeignKey(User, related_name="activity_type_insert_user", on_delete=models.DO_NOTHING)
    insert_date = models.DateTimeField()
    update_user = models.ForeignKey(User, related_name="activity_type_update_user", null=True, on_delete=models.DO_NOTHING)
    update_date = models.DateTimeField(null=True)
    
class Position(models.Model):
    alias = models.CharField(max_length=20, blank=False, null=False)
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=255)
    is_active = models.BooleanField(null=False)
    insert_user = models.ForeignKey(User, related_name="position_insert_user", on_delete=models.DO_NOTHING)
    insert_date = models.DateTimeField()
    update_user = models.ForeignKey(User, related_name="position_update_user", null=True, on_delete=models.DO_NOTHING)
    update_date = models.DateTimeField(null=True)
    
class MovementType(models.Model):
    alias = models.CharField(max_length=20, blank=False, null=False)
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=255)
    is_active = models.BooleanField(null=False)
    insert_user = models.ForeignKey(User, related_name="movement_type_insert_user", on_delete=models.DO_NOTHING)
    insert_date = models.DateTimeField()
    update_user = models.ForeignKey(User, related_name="movement_type_update_user", null=True, on_delete=models.DO_NOTHING)
    update_date = models.DateTimeField(null=True)
    
class Asset(models.Model):
    alias = models.CharField(max_length=20, blank=False, null=False)
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=255)
    is_active = models.BooleanField(null=False)
    insert_user = models.ForeignKey(User, related_name="asset_insert_user", on_delete=models.DO_NOTHING)
    insert_date = models.DateTimeField()
    update_user = models.ForeignKey(User, related_name="asset_update_user", null=True, on_delete=models.DO_NOTHING)
    update_date = models.DateTimeField(null=True)