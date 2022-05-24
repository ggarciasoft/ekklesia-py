from django.contrib import admin
from django_tenants.admin import TenantAdminMixin

# Register your models here.
from .models import EntityType, Organization
from .models import ActivityType
from .models import Position
from .models import MovementType
from .models import Asset

admin.site.register(EntityType)
admin.site.register(ActivityType)
admin.site.register(Position)
admin.site.register(Asset)
admin.site.register(MovementType)
admin.site.register(Organization)