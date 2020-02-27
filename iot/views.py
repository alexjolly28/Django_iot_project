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



class IotView(generics.GenericAPIView, mixins.ListModelMixin):
    queryset = IotModel.objects.all()
    serializer_class = IotModelSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        device_name = request.data['device_name']
        # status = request.data['status']
        queryset = IotModel.objects.get(device_name=device_name)
        serializer = IotModelSerializer(queryset)
        # json = JSONRenderer().render(serializer.data)
        # print(json)
        # data = json['']
        print(serializer.data['status'])

        # print(serializer.data['status'])

        # headers = self.get_success_headers(serializer.data)
        return Response(serializer.data)

# class IotView(APIView):
#     """
#     List all snippets, or create a new snippet.
#     """
#
#     def get_object(self):
#         try:
#             return IotModel.objects.all()
#         except IotModel.DoesNotExist:
#             raise status.HTTP_404_NOT_FOUND
#
#     def get(self, request):
#         iot = IotModel.objects.all()
#         serializer = IotModelSerializer(iot, many=True)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
#
#     def post(self, request, format=None):
#         # print(request.data)
#         # request.data.get("sheet")
#         queryset = IotModel.objects.get(id=2)
#
#         serializer = IotModelSerializer(queryset)
#         if serializer.is_valid():
#             print(serializer.data.get("device_name"))
#             #     serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
