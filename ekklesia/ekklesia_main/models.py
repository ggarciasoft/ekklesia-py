from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tenant(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=255)
    
class UserTenant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    
class Contact(models.Model):
    first_name = models.CharField(max_length=50, blank=False, null=True)
    last_name =  models.CharField(max_length=50, blank=False, null=False)
    email =  models.CharField(max_length=50, blank=False, null=True)
    address =  models.CharField(max_length=500, blank=False, null=True)
    home_phone =  models.CharField(max_length=10, blank=False, null=True)
    cell_phone =  models.CharField(max_length=10, blank=False, null=True)
    is_local_member =  models.BooleanField()
    birth_date = models.DateField(null=True)
    conversion_date = models.DateField(null=True)
    baptism_date = models.DateField(null=True)
    contact_image = models.ImageField(null=True)
    is_active =  models.BooleanField()
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    insert_user = models.ForeignKey(User, related_name="contact_insert_user", on_delete=models.DO_NOTHING)
    insert_date = models.DateTimeField()
    update_user = models.ForeignKey(User, related_name="contact_update_user", null=True, on_delete=models.DO_NOTHING)
    update_date = models.DateTimeField(null=True)
    
class EntityType(models.Model):
    alias = models.CharField(max_length=20, blank=False, null=False)
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=255)
    is_active = models.BooleanField(null=False)
    tenant = models.ForeignKey(Tenant, null=True, on_delete=models.CASCADE)
    insert_user = models.ForeignKey(User, related_name="entity_type_insert_user", on_delete=models.DO_NOTHING)
    insert_date = models.DateTimeField()
    update_user = models.ForeignKey(User, related_name="entity_type_update_user", null=True, on_delete=models.DO_NOTHING)
    update_date = models.DateTimeField(null=True)
    
class ActivityType(models.Model):
    alias = models.CharField(max_length=20, blank=False, null=False)
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=255)
    is_active = models.BooleanField(null=False)
    tenant = models.ForeignKey(Tenant, null=True, on_delete=models.CASCADE)
    insert_user = models.ForeignKey(User, related_name="activity_type_insert_user", on_delete=models.DO_NOTHING)
    insert_date = models.DateTimeField()
    update_user = models.ForeignKey(User, related_name="activity_type_update_user", null=True, on_delete=models.DO_NOTHING)
    update_date = models.DateTimeField(null=True)
    
class Activity(models.Model):
    activity_date = models.DateField()
    comments = models.CharField(max_length=500, blank=False, null=True)
    activity_type = models.ForeignKey(ActivityType, null=True, on_delete=models.SET_NULL)
    tenant = models.ForeignKey(Tenant, null=True, on_delete=models.CASCADE)
    insert_user = models.ForeignKey(User, related_name="activity_insert_user", on_delete=models.DO_NOTHING)
    insert_date = models.DateTimeField()
    update_user = models.ForeignKey(User, related_name="activity_update_user", null=True, on_delete=models.DO_NOTHING)
    update_date = models.DateTimeField(null=True)
    
class ActivityAssistant(models.Model):
    comments = models.CharField(max_length=500, blank=False, null=True)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, null=True, on_delete=models.CASCADE)
    entity_type = models.ForeignKey(EntityType, null=True, on_delete=models.SET_NULL)
    insert_user = models.ForeignKey(User, related_name="activity_assistant_insert_user", on_delete=models.DO_NOTHING)
    insert_date = models.DateTimeField()
    update_user = models.ForeignKey(User, related_name="activity_assistant_update_user", null=True, on_delete=models.DO_NOTHING)
    update_date = models.DateTimeField(null=True)
    
class Position(models.Model):
    alias = models.CharField(max_length=20, blank=False, null=False)
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=255)
    is_active = models.BooleanField(null=False)
    tenant = models.ForeignKey(Tenant, null=True, on_delete=models.CASCADE)
    insert_user = models.ForeignKey(User, related_name="position_insert_user", on_delete=models.DO_NOTHING)
    insert_date = models.DateTimeField()
    update_user = models.ForeignKey(User, related_name="position_update_user", null=True, on_delete=models.DO_NOTHING)
    update_date = models.DateTimeField(null=True)
    
class MovementType(models.Model):
    alias = models.CharField(max_length=20, blank=False, null=False)
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=255)
    is_active = models.BooleanField(null=False)
    tenant = models.ForeignKey(Tenant, null=True, on_delete=models.CASCADE)
    insert_user = models.ForeignKey(User, related_name="movement_type_insert_user", on_delete=models.DO_NOTHING)
    insert_date = models.DateTimeField()
    update_user = models.ForeignKey(User, related_name="movement_type_update_user", null=True, on_delete=models.DO_NOTHING)
    update_date = models.DateTimeField(null=True)
    
class Ministry(models.Model):
    alias = models.CharField(max_length=20, blank=False, null=False)
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=255)
    is_active = models.BooleanField(null=False)
    tenant = models.ForeignKey(Tenant, null=True, on_delete=models.CASCADE)
    insert_user = models.ForeignKey(User, related_name="ministry_insert_user", on_delete=models.DO_NOTHING)
    insert_date = models.DateTimeField()
    update_user = models.ForeignKey(User, related_name="ministry_update_user", null=True, on_delete=models.DO_NOTHING)
    update_date = models.DateTimeField(null=True)
    
class MemberMinistryPosition(models.Model):
    member = models.ForeignKey(Contact, on_delete=models.CASCADE)
    ministry = models.ForeignKey(Ministry, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    
class Asset(models.Model):
    alias = models.CharField(max_length=20, blank=False, null=False)
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=255)
    is_active = models.BooleanField(null=False)
    tenant = models.ForeignKey(Tenant, null=True, on_delete=models.CASCADE)
    insert_user = models.ForeignKey(User, related_name="asset_insert_user", on_delete=models.DO_NOTHING)
    insert_date = models.DateTimeField()
    update_user = models.ForeignKey(User, related_name="asset_update_user", null=True, on_delete=models.DO_NOTHING)
    update_date = models.DateTimeField(null=True)
    
class Movement(models.Model):
    movement_date = models.DateTimeField(null=False)
    comments = models.CharField(max_length=500, blank=False, null=True)
    activity = models.ForeignKey(Activity, null=True, on_delete=models.CASCADE)
    tenant = models.ForeignKey(Tenant, null=True, on_delete=models.CASCADE)
    insert_user = models.ForeignKey(User, related_name="movement_insert_user", on_delete=models.DO_NOTHING)
    insert_date = models.DateTimeField()
    update_user = models.ForeignKey(User, related_name="movement_update_user", null=True, on_delete=models.DO_NOTHING)
    update_date = models.DateTimeField(null=True)
    
class MovementDetail(models.Model):
    movement = models.ForeignKey(Movement, on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, null=True, on_delete=models.CASCADE)
    movement_type = models.ForeignKey(MovementType, on_delete=models.CASCADE)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    asset_quantity = models.FloatField()
    comments = models.CharField(max_length=500, blank=False, null=True)
    insert_user = models.ForeignKey(User, related_name="movement_detail_insert_user", on_delete=models.DO_NOTHING)
    insert_date = models.DateTimeField()
    update_user = models.ForeignKey(User, related_name="movement_detail_update_user", null=True, on_delete=models.DO_NOTHING)
    update_date = models.DateTimeField(null=True)