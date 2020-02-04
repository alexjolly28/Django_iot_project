from iot.models import IotModel
from iot.serialzers import IotModelSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class IotView(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get_object(self):
        try:
            return IotModel.objects.all()
        except IotModel.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request):
        iot = IotModel.objects.all()
        serializer = IotModelSerializer(iot, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        # print(request.data)
        # request.data.get("sheet")

        serializer = IotModelSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.data.get("device_name"))
            #     serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
