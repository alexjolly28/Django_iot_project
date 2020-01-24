from django.db import models


# Create your models here.
class IotModel(models.Model):
    device_name = models.CharField(max_length=200)
    status = models.CharField(max_length=10)
    colour = models.CharField(max_length=20)

    def __str__(self):
        return self.device_name
