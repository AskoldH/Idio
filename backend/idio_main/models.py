from django.db import models


class VideoSourcesType(models.Model):
    video_source_type = models.CharField(
        max_length=32, blank=False, null=False)
    label = models.CharField(max_length=32, blank=True, null=True)

    def __str__(self):
        return self.video_source_type


class VideoSourceName(models.Model):
    source_name_en = models.CharField(
        max_length=64, null=False, blank=False, default="/")
    source_name_cs = models.CharField(
        max_length=64, null=False, blank=False, default="/")
    source_season_episode = models.CharField(
        max_length=32, null=False, blank=False)

    def __str__(self):
        return (self.source_name_en + " | " + self.source_season_episode)


class EduVideo(models.Model):
    name = models.CharField(max_length=32, blank=False, null=False)
    video_file = models.FileField(upload_to='videos/', null=True)
    main_thought = models.CharField(max_length=64, null=True, blank=True)
    main_thought_false_1 = models.CharField(
        max_length=64, null=True, blank=True)
    main_thought_false_2 = models.CharField(
        max_length=64, null=True, blank=True)
    source_type = models.ForeignKey(
        VideoSourcesType, on_delete=models.CASCADE, blank=False, null=False)
    source_info = models.ForeignKey(
        VideoSourceName, on_delete=models.CASCADE, blank=False, null=False)

    def edu_video_save(self, *args, **kwargs):
        self.file.name = self.video_file
        super(EduVideoModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class SubtitlesInfo(models.Model):
    start_time = models.CharField(max_length=8, blank=False, null=False)
    original = models.CharField(max_length=128, null=True, blank=True)
    translation = models.CharField(max_length=128, null=True, blank=True)
    edu_video = models.ForeignKey(
        EduVideo, on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return (self.edu_video.name + " | " + self.start_time + " s")


class IdioUser(models.Model):
    cookie_value = models.CharField(max_length=13, blank=False, null=False)
    edu_videos_learned = models.ManyToManyField(
        EduVideo, through='EduVideosLearn', related_name="edu_videos_learned")
    edu_videos_skipped = models.ManyToManyField(
        EduVideo, through='EduVideosSkip', related_name="edu_videos_skipped")

    def __str__(self):
        return (self.cookie_value)


class EduVideosLearn(models.Model):
    edu_video = models.ForeignKey(
        EduVideo, on_delete=models.CASCADE, related_name="edu_video_learned")
    idio_user = models.ForeignKey(
        IdioUser, on_delete=models.CASCADE, related_name="idio_user_learned")


class EduVideosSkip(models.Model):
    edu_video = models.ForeignKey(
        EduVideo, on_delete=models.CASCADE, related_name="edu_video_skipped")
    idio_user = models.ForeignKey(
        IdioUser, on_delete=models.CASCADE, related_name="idio_user_skipped")
