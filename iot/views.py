from iot.models import IotModel
from iot.serialzers import IotModelSerializer
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import mixins
from .mqtt import on_publish
import json
from rest_framework.views import APIView
from rest_framework import status
from . import rasa_test


class IotView(generics.GenericAPIView, mixins.ListModelMixin):
    queryset = IotModel.objects.all()
    serializer_class = IotModelSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        json_data = json.loads(request.data)

        device_name = json_data['device_name']
        action = json_data['status']
        queryset = IotModel.objects.get(device_name=device_name)
        serializer = IotModelSerializer(queryset)
        # id = serializer.data['id']
        current_status = serializer.data['status']
        if current_status == action:
            print(device_name, "is already ", action)
            return Response(serializer.data)

        else:
            print("turning", action)
            on_publish(topic=device_name, payload=action)
            serializer = IotModelSerializer(queryset, data=json_data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EndView(APIView):
    def get(self, request):
        snippets = IotModel.objects.all()
        serializer = IotModelSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request):
        print(request.data)
        a = rasa_test.main(request.data)
        print(a)
        return Response(a, status=status.HTTP_200_OK)
