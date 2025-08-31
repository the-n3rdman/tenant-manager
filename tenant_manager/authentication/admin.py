from django.contrib import admin
from authentication.models import UserProfile, Entity

# Register your models here.

class EntityAdmin(admin.ModelAdmin):
    pass


class UserProfileAdmin(admin.ModelAdmin):
    pass


admin.site.register(Entity, EntityAdmin)
admin.site.register(UserProfile, UserProfileAdmin)