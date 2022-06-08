from django.contrib import admin
from datetime import datetime
# Register your models here.
from .models import EntityType, Organization
from .models import ActivityType
from .models import Position
from .models import MovementType
from .models import Asset

class CommonTypeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['alias', 'name', 'description', 'is_active']})
    ]
    def save_model(self, request, obj, form, change):
        if obj.id > 0:
            obj.update_user = request.user
            obj.update_date = datetime.now()
        else:
            obj.insert_user = request.user
        obj.save()

admin.site.register(EntityType, CommonTypeAdmin)
admin.site.register(ActivityType, CommonTypeAdmin)
admin.site.register(Position, CommonTypeAdmin)
admin.site.register(Asset, CommonTypeAdmin)
admin.site.register(MovementType, CommonTypeAdmin)
admin.site.register(Organization)