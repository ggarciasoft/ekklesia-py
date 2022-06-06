from django.contrib import admin

from .models import Contact
from .models import Activity
from .models import ActivityAssistant
from .models import MemberMinistryPosition
from .models import Movement
from .models import MovementDetail

class MovementDetailInline(admin.TabularInline):
    model = MovementDetail
    extra = 3

class MovementAdmin(admin.ModelAdmin):
    inlines = [MovementDetailInline]


admin.site.register(Contact)
admin.site.register(Activity)
admin.site.register(ActivityAssistant)
admin.site.register(MemberMinistryPosition)
admin.site.register(Movement, MovementAdmin)