from django.contrib import admin
from .models import EduVideo, SubtitlesInfo, IdioUser, EduVideosLearn, EduVideosSkip, VideoSourceName, VideoSourcesType

admin.site.register(EduVideo)
admin.site.register(SubtitlesInfo)
admin.site.register(IdioUser)
admin.site.register(EduVideosLearn)
admin.site.register(EduVideosSkip)
admin.site.register(VideoSourceName)
admin.site.register(VideoSourcesType)