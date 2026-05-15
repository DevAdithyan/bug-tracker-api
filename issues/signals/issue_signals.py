from django.db.models.signals import post_save
from django.dispatch import receiver

from issues.models import Issue
from notifications.models import Notification


@receiver(post_save, sender=Issue)
def create_issue_notification(sender, instance, created, **kwargs):

    if created and instance.assigned_to:

        Notification.objects.create(
            user=instance.assigned_to,
            message=f"You were assigned issue: {instance.title}"
        )

        