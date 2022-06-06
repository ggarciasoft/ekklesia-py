from django.db import models
from django.contrib.auth.models import User
#from django.contrib.auth.models import User
from ekklesia_shared.models import ActivityType, EntityType, MovementType, Position, Asset

# Create your models here.
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
    insert_user = models.ForeignKey(User, related_name="contact_insert_user", on_delete=models.DO_NOTHING)
    insert_date = models.DateTimeField(auto_now_add=True)
    update_user = models.ForeignKey(User, related_name="contact_update_user", null=True, on_delete=models.DO_NOTHING)
    update_date = models.DateTimeField(null=True)
    def __str__(self):
        return self.first_name 
    
class Activity(models.Model):
    activity_date = models.DateField()
    comments = models.CharField(max_length=500, blank=False, null=True)
    activity_type = models.ForeignKey(ActivityType, null=True, on_delete=models.SET_NULL)
    insert_user = models.ForeignKey(User, related_name="activity_insert_user", on_delete=models.DO_NOTHING)
    insert_date = models.DateTimeField(auto_now_add=True)
    update_user = models.ForeignKey(User, related_name="activity_update_user", null=True, on_delete=models.DO_NOTHING)
    update_date = models.DateTimeField(null=True)
    def __str__(self):
        return self.activity_date 
    
class ActivityAssistant(models.Model):
    comments = models.CharField(max_length=500, blank=False, null=True)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, null=True, on_delete=models.CASCADE)
    entity_type = models.ForeignKey(EntityType, null=True, on_delete=models.SET_NULL)
    insert_user = models.ForeignKey(User, related_name="activity_assistant_insert_user", on_delete=models.DO_NOTHING)
    insert_date = models.DateTimeField(auto_now_add=True)
    update_user = models.ForeignKey(User, related_name="activity_assistant_update_user", null=True, on_delete=models.DO_NOTHING)
    update_date = models.DateTimeField(null=True)
    
class Ministry(models.Model):
    alias = models.CharField(max_length=20, blank=False, null=False)
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=255)
    is_active = models.BooleanField(null=False)
    insert_user = models.ForeignKey(User, related_name="ministry_insert_user", on_delete=models.DO_NOTHING)
    insert_date = models.DateTimeField(auto_now_add=True)
    update_user = models.ForeignKey(User, related_name="ministry_update_user", null=True, on_delete=models.DO_NOTHING)
    update_date = models.DateTimeField(null=True)
    def __str__(self):
        return self.name 
    
class MemberMinistryPosition(models.Model):
    member = models.ForeignKey(Contact, on_delete=models.CASCADE)
    ministry = models.ForeignKey(Ministry, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    
class Movement(models.Model):
    movement_date = models.DateTimeField(null=False)
    comments = models.CharField(max_length=500, blank=False, null=True)
    activity = models.ForeignKey(Activity, null=True, on_delete=models.CASCADE)
    insert_user = models.ForeignKey(User, related_name="movement_insert_user", on_delete=models.DO_NOTHING)
    insert_date = models.DateTimeField(auto_now_add=True)
    update_user = models.ForeignKey(User, related_name="movement_update_user", null=True, on_delete=models.DO_NOTHING)
    update_date = models.DateTimeField(null=True)
    def __str__(self):
        return self.movement_date 
    
class MovementDetail(models.Model):
    movement = models.ForeignKey(Movement, on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, null=True, on_delete=models.CASCADE)
    movement_type = models.ForeignKey(MovementType, on_delete=models.CASCADE)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    asset_quantity = models.FloatField()
    comments = models.CharField(max_length=500, blank=False, null=True)
    insert_user = models.ForeignKey(User, related_name="movement_detail_insert_user", on_delete=models.DO_NOTHING)
    insert_date = models.DateTimeField(auto_now_add=True)
    update_user = models.ForeignKey(User, related_name="movement_detail_update_user", null=True, on_delete=models.DO_NOTHING)
    update_date = models.DateTimeField(null=True)
    def __str__(self):
        return self.movement_type 