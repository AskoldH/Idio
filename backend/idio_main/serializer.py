from rest_framework.serializers import ModelSerializer
from .models import EduVideo

class EduVideoSerializer(ModelSerializer):
    class Meta:
        model = EduVideo
        fields = ["id", "name", "video_file"]
