from .models import EduVideo, SubtitlesInfo, EduVideosLearn, EduVideosSkip, IdioUser
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .serializer import EduVideoSerializer, SubtitlesInfoSerializer, IdioUserSerializer, EduVideoLearnSerializer, EduVideoSkipSerializer
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.views import APIView


class EduVideosViewSet(APIView):
    serializer_class = EduVideoSerializer

    queryset = EduVideo.objects.all()

    def get(self, request, *args, **kwargs):
        user_cookie_value = request.query_params.get("user-cookie-value")
        print(user_cookie_value)

        idio_user = IdioUser.objects.get(cookie_value=user_cookie_value)

        to_exclude_learned = EduVideosLearn.objects.filter(
            idio_user=idio_user).values('edu_video')
        to_exclude_skipped = EduVideosSkip.objects.filter(
            idio_user=idio_user).values('edu_video')

        all_ids = []
        for pair in list(to_exclude_learned):
            all_ids.append(pair.get('edu_video'))

        for pair in list(to_exclude_skipped):
            all_ids.append(pair.get('edu_video'))

        edu_video = self.queryset.exclude(id__in=all_ids)
        serializer = EduVideoSerializer(edu_video.first())
        return Response(serializer.data)


class SubtitlesInfoViewSet(APIView):
    serializer_class = SubtitlesInfoSerializer

    queryset = SubtitlesInfo.objects.all()

    def get(self, request, *args, **kwargs):
        edu_video_id = request.query_params.get("edu-video-id")
        print("edu id", edu_video_id)

        subtitles_infos = self.queryset.filter(edu_video=edu_video_id)
        serializer = SubtitlesInfoSerializer(subtitles_infos, many=True)
        return Response(serializer.data)


class IdioUserViewSet(APIView):
    serializer_class = IdioUserSerializer

    def get_queryset(self):
        queryset = IdioUser.objects.all()
        return queryset

    def get(self, request, *args, **kwargs):
        serializer = IdioUserSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        user_data = request.data
        print(user_data)
        new_user = IdioUser.objects.create(
            cookie_value=str(user_data["user_cookie_value"]))
        print(new_user)
        new_user.save()

        serializer = IdioUserSerializer(new_user)

        return Response(serializer.data)


class EduVideoLearnViewSet(APIView):
    serializer_class = EduVideoLearnSerializer

    def get_queryset(self):
        queryset = EduVideosLearn.objects.all()
        return queryset

    def get(self, request, *args, **kwargs):
        serializer = EduVideoLearnSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        new_edu_video_learn = EduVideosLearn.objects.create(
            edu_video=EduVideo.objects.get(id=request.data["edu_video_id"]),
            idio_user=IdioUser.objects.get(cookie_value=request.data["cookie_value"]))
        print(new_edu_video_learn)
        new_edu_video_learn.save()

        serializer = EduVideoLearnSerializer(new_edu_video_learn)

        return Response(serializer.data)

class EduVideoSkipViewSet(APIView):
    serializer_class = EduVideoSkipSerializer

    def get_queryset(self):
        queryset = EduVideosLearn.objects.all()
        return queryset

    def get(self, request, *args, **kwargs):
        serializer = EduVideoLearnSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        new_edu_video_skip = EduVideosSkip.objects.create(
            edu_video=EduVideo.objects.get(id=request.data["edu_video_id"]),
            idio_user=IdioUser.objects.get(cookie_value=request.data["cookie_value"]))
        new_edu_video_skip.save()

        serializer = EduVideoSkipSerializer(new_edu_video_skip)

        return Response(serializer.data)