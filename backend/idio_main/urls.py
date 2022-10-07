from rest_framework import routers
from .views import EduVideosViewSet

router = routers.DefaultRouter()

router.register('api/edu-videos', EduVideosViewSet)

urlpatterns = router.urls
