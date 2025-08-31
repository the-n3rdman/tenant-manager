from django.contrib import admin
from settings.models import (Location, Building, Floor, Room, Bed, Amenity, AmenityDeploymentMap, 
                             Tenant, TenantAmenityMap, PaymentHistory, Document, TenantDocumentMap)
# Register your models here.


class LocationAdmin(admin.ModelAdmin):
    pass

class BuildingAdmin(admin.ModelAdmin):
    pass

class FloorAdmin(admin.ModelAdmin):
    pass

class RoomAdmin(admin.ModelAdmin):
    pass

class BedAdmin(admin.ModelAdmin):
    pass

class AmenityAdmin(admin.ModelAdmin):
    pass

class AmenityDeploymentMapAdmin(admin.ModelAdmin):
    pass

class TenantAdmin(admin.ModelAdmin):
    pass

class TenantAmenityMapAdmin(admin.ModelAdmin):
    pass

class DocumentAdmin(admin.ModelAdmin):
    pass

class TenantDocumentMapAdmin(admin.ModelAdmin):
    pass

class PaymentHistoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Location, LocationAdmin)
admin.site.register(Building, BuildingAdmin)
admin.site.register(Floor, FloorAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Bed, BedAdmin)
admin.site.register(Amenity, AmenityAdmin)
admin.site.register(AmenityDeploymentMap, AmenityDeploymentMapAdmin)
admin.site.register(Tenant, TenantAdmin)
admin.site.register(TenantAmenityMap, TenantAmenityMapAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(TenantDocumentMap, TenantDocumentMapAdmin)
admin.site.register(PaymentHistory, PaymentHistoryAdmin)