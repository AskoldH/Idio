from rest_framework.serializers import ModelSerializer
from .models import EduVideo, SubtitlesInfo

class EduVideoSerializer(ModelSerializer):
    class Meta:
        model = EduVideo
        fields = ["id", "name", "video_file", "source_type", "source_info"]

class SubtitlesInfoSerializer(ModelSerializer):
    class Meta:
        model = SubtitlesInfo
        fields = ["id", "start_time", "original", "translation"]

