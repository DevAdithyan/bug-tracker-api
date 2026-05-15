from django.db import models
from django.conf import settings

from issues.models import Issue


class Comment(models.Model):

    issue = models.ForeignKey(
        Issue,
        on_delete=models.CASCADE,
        related_name='comments'
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    text = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.issue.title}"