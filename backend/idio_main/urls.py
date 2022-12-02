from rest_framework import routers
from .views import EduVideosViewSet, SubtitlesInfoViewSet

router = routers.DefaultRouter()

router.register(r'api/edu-video', EduVideosViewSet, basename='EduVideos')
router.register(r'api/subtitles-info', SubtitlesInfoViewSet, basename='SubtitlesInfo')

urlpatterns = router.urls
