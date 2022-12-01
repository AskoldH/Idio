from django.db import models


class EduVideo(models.Model):
    FILM = "FILM"
    TV_SERIES = "TV-SERIES"
    MUSIC_CLIP = "MUSIC_CLIP"
    OTHER = "OTHER"

    SOURCE_TYPE_CHOICES = ((FILM, "film"),
                           (TV_SERIES, "TV-series"),
                           (MUSIC_CLIP, "music clip"),
                           (OTHER, "other")
                           )

    name = models.CharField(max_length=32, blank=False, null=False)
    video_file = models.FileField(upload_to='videos/', null=True)
    main_thought = models.CharField(max_length=64, null=True, blank=True)
    source_type = models.CharField(max_length=32, choices=SOURCE_TYPE_CHOICES, blank=False, default=OTHER)
    source_info = models.CharField(max_length=64, null=True, blank=True)

    def __str__(self):
        return self.name


class SubtitlesInfo(models.Model):
    start_time = models.CharField(max_length=8, blank=False, null=False)
    original = models.CharField(max_length=128, null=True, blank=True)
    translation = models.CharField(max_length=128, null=True, blank=True)
    edu_video = models.ForeignKey(EduVideo, on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return (self.edu_video.name + " | " + self.start_time + " s")
