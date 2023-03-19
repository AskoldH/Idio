from rest_framework.serializers import ModelSerializer
from .models import EduVideo, SubtitlesInfo, IdioUser, EduVideosLearn, EduVideosSkip, VideoSourcesType, VideoSourceName
from rest_framework import serializers

class EduVideoSerializer(ModelSerializer):
    class Meta: 
        model = EduVideo
        fields = ["id", "name", "video_file", "source_type", "source_info", "main_thought", "main_thought_false_1",
                    "main_thought_false_2"]

class SubtitlesInfoSerializer(ModelSerializer):
    class Meta:
        model = SubtitlesInfo
        fields = ["id", "start_time", "original", "translation"]

class IdioUserSerializer(ModelSerializer):
    class Meta:
        model = IdioUser
        fields = ["cookie_value", "last_edu_video", "check_test"]

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
        fields = ["video_source_type", "label"]

class VideoSourceNameSerializer(ModelSerializer):
    class Meta:
        model = VideoSourceName
        fields = ["source_name_en", "source_name_cs", "source_season_episode"]
