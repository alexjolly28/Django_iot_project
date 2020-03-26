import requests
import json

a = {}
url = 'http://127.0.0.1:5005/model/parse'

api_url = 'http://127.0.0.1:8000/iot/'


def main(text):
    x = requests.post(url, json=text)

    data = x.text
    json_data = json.loads(data)
    entities = json_data["entities"]
    intents = json_data["intent"]
    acc = intents["confidence"]
    if acc >= .9:
        device = intents["name"]
        a["device_name"] = device
        for entity in entities:
            if entity["entity"] == "action":
                a["status"] = entity["value"]
            if entity["entity"] == "value":
                a["colour"] = entity["value"]

    json_a = json.dumps(a)
    resp = requests.post(api_url, json=json_a)
    # print(resp)
    return (True)


# if __name__ == '__main__':
#     text = {"text": "turn  off green light  "}
#
#     data_json = main(text)
#     print(data_json)
#     # test_json = {"device_name": "fan", "status": "off"}
#     resp = requests.post(api_url, json=data_json)
#     print(resp)
