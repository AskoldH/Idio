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


class IdioUser(models.Model):
    cookie_value = models.CharField(max_length=13, blank=False, null=False)
    edu_videos_learned = models.ManyToManyField(EduVideo, through='EduVideosLearn', related_name="edu_videos_learned")
    edu_videos_skipped = models.ManyToManyField(EduVideo, through='EduVideosSkip', related_name="edu_videos_skipped")

    def __str__(self):
        return (self.cookie_value)

class EduVideosLearn(models.Model):
    edu_video = models.ForeignKey(EduVideo, on_delete=models.CASCADE, related_name="edu_video_learned")
    idio_user = models.ForeignKey(IdioUser, on_delete=models.CASCADE, related_name="idio_user_learned")

class EduVideosSkip(models.Model):
    edu_video = models.ForeignKey(EduVideo, on_delete=models.CASCADE, related_name="edu_video_skipped")
    idio_user = models.ForeignKey(IdioUser, on_delete=models.CASCADE, related_name="idio_user_skipped")