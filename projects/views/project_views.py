from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from projects.models import Project
from projects.serializers.project_serializer import ProjectSerializer

from common.permissions.is_admin import IsAdminUserRole


class ProjectViewSet(ModelViewSet):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_permissions(self):

        if self.action in ['create', 'update', 'destroy']:
            permission_classes = [IsAdminUserRole]
        else:
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):

        serializer.save(created_by=self.request.user)