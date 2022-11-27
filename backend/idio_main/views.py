from .models import EduVideo, SubtitlesInfo
from rest_framework.viewsets import ModelViewSet
from .serializer import EduVideoSerializer, SubtitlesInfoSerializer


class EduVideosViewSet(ModelViewSet):
    serializer_class = EduVideoSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = EduVideo.objects.all()
        return queryset

class SubtitlesInfoViewSet(ModelViewSet):
    serializer_class = SubtitlesInfoSerializer

    def get_queryset(self, *args, **kwargs):
        edu_video_id = self.request.query_params.get('eduvideo-id')
        queryset = SubtitlesInfo.objects.filter(edu_video_id=edu_video_id)
        return queryset