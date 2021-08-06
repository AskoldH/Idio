from rest_framework.response import Response
from rest_framework import generics
from .models import Idiom
from .serializers import IdiomSerializer


class IdiomView(generics.RetrieveAPIView):
    queryset = Idiom.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = IdiomSerializer(queryset, many=True)
        return Response(serializer.data)