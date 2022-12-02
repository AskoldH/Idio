from .models import EduVideo, SubtitlesInfo, EduVideosLearn, EduVideosSkip, IdioUser
from rest_framework.viewsets import ModelViewSet
from .serializer import EduVideoSerializer, SubtitlesInfoSerializer
from django.db.models import Q


class EduVideosViewSet(ModelViewSet):
    serializer_class = EduVideoSerializer

    def get_queryset(self, *args, **kwargs):
        user_cookie_value = self.request.query_params.get('cookie-value')
        print(user_cookie_value)

        idio_user = IdioUser.objects.get(cookie_value=user_cookie_value)
        learned_to_exclude = EduVideosLearn.objects.filter(idio_user=idio_user)
        skipped_to_exclude = EduVideosSkip.objects.filter(idio_user=idio_user)

        print("learned", EduVideosLearn.objects.filter(
            idio_user=idio_user).values_list('edu_video'))
        print("skipped", EduVideosSkip.objects.filter(
            idio_user=idio_user).values('edu_video'))

        queryset_all = EduVideo.objects.all()
        print("all", queryset_all)

        # queryset_part = EduVideo.objects.filter(
        # id__in=EduVideosLearn.objects.filter(idio_user=idio_user).values('edu_video'))

        to_exclude_learned = EduVideosLearn.objects.filter(
            idio_user=idio_user).values('edu_video')
        to_exclude_skipped = EduVideosSkip.objects.filter(
            idio_user=idio_user).values('edu_video')

        all_ids = EduVideo.objects.all().values('id')

        all_ids_list = []
        for pair in list(all_ids):
            all_ids_list.append(pair['id'])

        for pair in list(to_exclude_learned):
            all_ids_list.remove(pair['edu_video'])

        for pair in list(to_exclude_skipped):
            all_ids_list.remove(pair['edu_video'])

        print(all_ids_list)
        queryset = EduVideo.objects.filter(id__in=all_ids_list)
        print(queryset)

        return queryset


class SubtitlesInfoViewSet(ModelViewSet):
    serializer_class = SubtitlesInfoSerializer

    def get_queryset(self, *args, **kwargs):
        edu_video_id = self.request.query_params.get('edu-video-id')
        queryset = SubtitlesInfo.objects.filter(edu_video_id=edu_video_id)
        return queryset
