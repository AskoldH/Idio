from rest_framework import serializers
from .models import Idiom

class IdiomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idiom
        fields = '__all__'