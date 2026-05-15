from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from issues.models import Issue
from issues.serializers.issue_serializer import IssueSerializer


class IssueViewSet(ModelViewSet):

    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):

        serializer.save(created_by=self.request.user)