from iot.models import IotModel
from iot.serialzers import IotModelSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework import status
from rest_framework import generics
from rest_framework import mixins
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .mqtt import on_publish


class IotView(generics.GenericAPIView, mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin):
    queryset = IotModel.objects.all()
    serializer_class = IotModelSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        device_name = request.data['device_name']
        status = request.data['status']
        queryset = IotModel.objects.get(device_name=device_name)
        serializer = IotModelSerializer(queryset)
        # id = serializer.data['id']
        current_status = serializer.data['status']
        if current_status == status:
            print("it is alredy ", status)
            return Response(serializer.data)

        else:
            print("turning", status)
            on_publish(topic=device_name, payload=status)
            serializer = IotModelSerializer(queryset, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
