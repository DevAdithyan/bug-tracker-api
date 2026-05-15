from django.contrib import admin
from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'issue',
        'user',
        'created_at',
    )

    search_fields = (
        'issue__title',
        'user__username',
        'text',
    )

    list_filter = (
        'created_at',
    )

    ordering = (
        '-created_at',
    )

    readonly_fields = (
        'created_at',
    )