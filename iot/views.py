from iot.models import IotModel
from iot.serialzers import IotModelSerializer
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import mixins
from .mqtt import on_publish
import json


class IotView(generics.GenericAPIView, mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin):
    queryset = IotModel.objects.all()
    serializer_class = IotModelSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        json_data = json.loads(request.data)

        device_name = json_data['device_name']
        status = json_data['status']
        queryset = IotModel.objects.get(device_name=device_name)
        serializer = IotModelSerializer(queryset)
        # id = serializer.data['id']
        current_status = serializer.data['status']
        if current_status == status:
            print(device_name, "is alredy ", status)
            return Response(serializer.data)

        else:
            print("turning", status)
            on_publish(topic=device_name, payload=status)
            serializer = IotModelSerializer(queryset, data=json_data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            print("ok")
            return Response(serializer.errors)

