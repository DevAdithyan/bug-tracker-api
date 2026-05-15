from django.contrib import admin
from .models import Issue


@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'title',
        'project',
        'status',
        'priority',
        'created_by',
        'assigned_to',
        'created_at',
    )

    list_filter = (
        'status',
        'priority',
        'project',
        'created_at',
    )

    search_fields = (
        'title',
        'description',
        'project__name',
        'created_by__username',
        'assigned_to__username',
    )

    ordering = (
        '-created_at',
    )

    readonly_fields = (
        'created_at',
        'updated_at',
    )