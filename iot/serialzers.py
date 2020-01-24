from rest_framework import serializers
from .models import IotModel


class IotModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = IotModel
        fields = ('id','url', 'device_name', 'status', 'colour')

