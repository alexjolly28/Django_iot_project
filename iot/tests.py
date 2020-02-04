from django.test import TestCase
import requests
data = {'device_name':'ima',
        'status':'on',
        'colour':'kara',}
r = requests.post('http://127.0.0.1:8000/iot/', data=data)