from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from comments.models import Comment
from comments.serializers.comment_serializer import CommentSerializer


class CommentViewSet(ModelViewSet):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):

        serializer.save(user=self.request.user)