#! /usr/bin/python
import paho.mqtt.client
import time

def mqtt_callback(client, user_data, message):
    print("Message with topic {} received: {}".format(message.topic, str(message.payload.decode("utf-8"))))

device = "127.0.0.1"
topic1 = "/junos/events/kernel/route/#"

if __name__ == "__main__":
    print "connecting to MQTT brocker"
    client = paho.mqtt.client.Client()
    client.connect(device)
    client.loop_start()
    client.on_message = mqtt_callback
    
    client.subscribe(topic1)

    time.sleep(60)

 #   raw_input("Press Enter to stop \n\n\n")
    client.loop_stop()
    client.disconnect()