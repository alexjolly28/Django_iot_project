from rest_framework.serializers import ModelSerializer
from .models import IotModel


class IotModelSerializer(ModelSerializer):
    class Meta:
        model = IotModel
        fields = '__all__'

