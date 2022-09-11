from rest_framework import serializers
from .models import Datchik, Temp

class DatchikSerializer(serializers.ModelSerializer):
    class Meta:
        model = Datchik
        fields = ['id','name', 'description', 'measurements']


class MeasureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temp
        fields = ['sensor', 'temperature']


# TODO: опишите необходимые сериализаторы
