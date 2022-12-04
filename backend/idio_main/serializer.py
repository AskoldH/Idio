from rest_framework.serializers import ModelSerializer
from .models import EduVideo, SubtitlesInfo, IdioUser, EduVideosLearn, EduVideosSkip, VideoSourcesType, VideoSourceName

class EduVideoSerializer(ModelSerializer):
    class Meta: 
        model = EduVideo
        fields = ["id", "name", "video_file", "source_type", "source_info"]

class SubtitlesInfoSerializer(ModelSerializer):
    class Meta:
        model = SubtitlesInfo
        fields = ["id", "start_time", "original", "translation"]

class IdioUserSerializer(ModelSerializer):
    class Meta:
        model = IdioUser
        fields = ["cookie_value"]

class EduVideoLearnSerializer(ModelSerializer):
    class Meta:
        model = EduVideosLearn
        fields = ["edu_video", "idio_user"]

class EduVideoSkipSerializer(ModelSerializer):
    class Meta:
        model = EduVideosSkip
        fields = ["edu_video", "idio_user"]

class VideoSourceTypeSerializer(ModelSerializer):
    class Meta:
        model = VideoSourcesType
        fields = ["video_source_type"]

class VideoSourceNameSerializer(ModelSerializer):
    class Meta:
        model = VideoSourceName
        fields = ["source_name", "source_season_episode"]
