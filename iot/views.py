from django.shortcuts import render
from .models import IotModel
from rest_framework import viewsets
from .serialzers import IotModelSerializer


class IotModelView(viewsets.ModelViewSet):
    queryset = IotModel.objects.all()
    serializer_class = IotModelSerializer
