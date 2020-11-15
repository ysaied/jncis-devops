#! /usr/bin/python
import paho.mqtt.client

def mqtt_callback(client, user_data, message):
    print("Message with topic {} received: {}".format(message.topic, str(message.payload.decode("utf-8"))))

device = "3.126.37.30"
topic1 = "/junos/events/kernel/route/add/#"
topic2 = "/junos/events/kernel/route/delete/#"

if if __name__ == "__main__":
    print "connecting to MQTT brocker"
    client = paho.mqtt.client.Client("client1")
    client.on_message = mqtt_callback
    client.connect(device)
    client.loop_start()
    client.subscribe(topic1)
    client.subscribe(topic2)
    raw_input("Press Enter to sopt")
    client.loopstop()
    client.disconnect()