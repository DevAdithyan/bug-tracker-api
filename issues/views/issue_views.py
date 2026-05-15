from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from issues.models import Issue
from issues.serializers.issue_serializer import IssueSerializer


class IssueViewSet(ModelViewSet):

    queryset = Issue.objects.select_related('project','created_by','assigned_to').all()
    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated]

    filterset_fields = ['status', 'priority', 'project']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at', 'priority']

    def perform_create(self, serializer):

        serializer.save(created_by=self.request.user)