from .models import EduVideo, SubtitlesInfo, EduVideosLearn, EduVideosSkip, IdioUser, VideoSourceName, VideoSourcesType
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .serializer import EduVideoSerializer, SubtitlesInfoSerializer, IdioUserSerializer, EduVideoLearnSerializer, EduVideoSkipSerializer, VideoSourceNameSerializer
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.views import APIView
import random


class EduVideosViewSet(APIView):
    serializer_class = EduVideoSerializer

    queryset = EduVideo.objects.all()

    def get(self, request, *args, **kwargs):
        idio_user = IdioUser.objects.get(cookie_value=str(
            request.query_params.get('cookie_value')))
        button_type = str(request.query_params.get('button_type'))
        edu_video_id_param = str(request.query_params.get('edu_video_id'))

        if button_type == "back":
            edu_video_id = idio_user.last_edu_video.id
            edu_video = EduVideo.objects.get(id=edu_video_id)

            learn_video_object = EduVideosLearn.objects.filter(
                edu_video=edu_video_id)
            if learn_video_object.exists():
                learn_video_object.delete()

            skip_video_object = EduVideosSkip.objects.filter(
                edu_video=edu_video_id)
            if skip_video_object.exists():
                skip_video_object.delete()
        else:
            if edu_video_id_param != "false":
                if button_type == "skip":
                    new_edu_video_skip = EduVideosSkip.objects.create(
                        edu_video=EduVideo.objects.get(
                        id=edu_video_id_param),
                        idio_user=idio_user)
                    new_edu_video_skip.save()

                elif button_type == "learned":
                    new_edu_video_learn = EduVideosLearn.objects.create(
                        edu_video=EduVideo.objects.get(id=edu_video_id_param),
                        idio_user=idio_user)
                    new_edu_video_learn.save()

            to_exclude_learned = EduVideosLearn.objects.filter(
             idio_user=idio_user).values('edu_video')
            to_exclude_skipped = EduVideosSkip.objects.filter(
              idio_user=idio_user).values('edu_video')

            all_ids = []
            for pair in list(to_exclude_learned):
                all_ids.append(pair.get('edu_video'))

            for pair in list(to_exclude_skipped):
                all_ids.append(pair.get('edu_video'))

            if idio_user.last_edu_video != None:
                all_ids.append(idio_user.last_edu_video.id)

            edu_videos = self.queryset.exclude(id__in=all_ids)
            random_index = random.randint(0, edu_videos.count() - 1)
            edu_video = edu_videos[random_index]

        serializer = EduVideoSerializer(edu_video)
        video_source_name_serializer = VideoSourceNameSerializer(
            VideoSourceName.objects.get(id=serializer.data.get("source_info")))
        source_data = video_source_name_serializer.data
        data = serializer.data

        data.update(source_data)
        return Response(data)


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

    queryset = IdioUser.objects.all()


    def get(self, request, *args, **kwargs):
        cookie_value = request.query_params.get("cookie_value")
        serializer = IdioUserSerializer(IdioUser.objects.get(cookie_value=cookie_value))
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

    def patch(self, request, *args, **kwargs):
        idio_user = IdioUser.objects.get(
            cookie_value=request.data["cookie_value"])
        edu_video = EduVideo.objects.get(id=request.data["edu_video_id"])

        idio_user.last_edu_video = edu_video
        idio_user.save()
        return Response(status=200)


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
