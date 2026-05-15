from rest_framework.routers import DefaultRouter

from comments.views.comment_views import CommentViewSet


router = DefaultRouter()

router.register('', CommentViewSet, basename='comments')

urlpatterns = router.urls