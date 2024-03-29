from rest_framework import routers
from .views import EduVideosViewSet, SubtitlesInfoViewSet, IdioUserViewSet, EduVideoLearnViewSet, EduVideoSkipViewSet
from django.conf.urls import url

urlpatterns = [
    url('api/edu-video-learn', EduVideoLearnViewSet.as_view()),
    url('api/edu-video-skip', EduVideoSkipViewSet.as_view()),
    url('api/edu-video', EduVideosViewSet.as_view()),
    url('api/subtitles-info', SubtitlesInfoViewSet.as_view()),
    url('api/idio-user', IdioUserViewSet.as_view()),
    ]



