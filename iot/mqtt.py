import paho.mqtt.client as mqtt
import time

broker_url = "localhost"
broker_port = 1883


def on_connect(client, userdata, flags, rc):
    print("Connected With Result Code "(rc))


def on_message_from_kitchen(client, userdata, message):
    print("Message Recieved from Kitchen: " + message.payload.decode())


def on_message_from_bedroom(client, userdata, message):
    print("Message Recieved from Bedroom: " + message.payload.decode())


def on_message(client, userdata, message):
    print("Message Recieved from Others: " + message.payload.decode())


def on_publish(topic, payload):
    client.publish(topic=topic, payload=payload, qos=1, retain=False)


client = mqtt.Client()
client.on_connect = on_connect
# To Process Every Other Message
client.on_message = on_message
client.connect(broker_url, broker_port)

# client.subscribe("test", qos=1)
# client.subscribe("test1", qos=1)
# client.subscribe("test2", qos=1)
# client.message_callback_add("test1", on_message_from_kitchen)
# client.message_callback_add("test2", on_message_from_bedroom)
# client.loop_start()
# time.sleep(5)
# on_publish(topic="test1", payload="pub")
# time.sleep(5)
#
# client.loop_stop()
# client.loop_forever()
