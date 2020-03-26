from django.urls import path, include
from iot.views import IotView,EndView

# from rest_framework import routers
#
# # router = routers.DefaultRouter()
# # router.register('iot', views.IotView)
urlpatterns = [
    path('iot/', IotView.as_view(), name='iotview'),
    path('end/', EndView.as_view(), name='endview'),
]
