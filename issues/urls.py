from rest_framework.routers import DefaultRouter

from issues.views.issue_views import IssueViewSet


router = DefaultRouter()

router.register('', IssueViewSet, basename='issues')

urlpatterns = router.urls