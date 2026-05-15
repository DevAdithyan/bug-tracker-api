from rest_framework.routers import DefaultRouter

from projects.views.project_views import ProjectViewSet


router = DefaultRouter()

router.register('', ProjectViewSet, basename='projects')

urlpatterns = router.urls