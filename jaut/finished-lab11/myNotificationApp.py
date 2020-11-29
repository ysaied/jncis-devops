from paho.mqtt.client import Client

DEVICE = "172.25.11.1"
TOPIC = "/junos/events/kernel/firewall/filter/#"

def callback(client, data, message):
    print "Message with topic %s received: %s" % (message.topic, message.payload)

if __name__ == "__main__":
    print "Connecting to MQTT broker"
    client = Client()
    client.on_message = callback
    client.connect(DEVICE)
    client.loop_start()
    client.subscribe(TOPIC)
    raw_input("Press Enter to stop")
    client.loop_stop()
    client.disconnect()
