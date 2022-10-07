from django.db import models


class EduVideo(models.Model):
    name = models.CharField(max_length=32)
    video_file = models.FileField(upload_to='videos/', null=True)
    subtitles_original_language = models.JSONField(blank=False )

    def __str__(self):
        return self.name + ": " + str(self.video_file)
