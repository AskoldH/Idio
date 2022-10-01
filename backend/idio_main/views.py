
from .models import EduVideo
from rest_framework.viewsets import ModelViewSet
from .serializer import EduVideoSerializer
class EduVideosViewSet(ModelViewSet):
    queryset = EduVideo.objects.all()
    serializer_class = EduVideoSerializer