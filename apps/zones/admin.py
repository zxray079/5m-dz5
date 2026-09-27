from django.contrib import admin

from .models import Zone, Visitors


@admin.register(Zone)
class ZoneAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'location',
        'visitors',
        'latitude',
        'longitude',
        'created_at',
    )

    list_filter = (
        'created_at',
    )

    search_fields = (
        'location',
    )


@admin.register(Visitors)
class VisitorsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'zone',
        'is_allowed',
        'created_at',
    )

    list_filter = (
        'is_allowed',
        'zone',
        'created_at',
    )

    search_fields = (
        'name',
        'information',
    )