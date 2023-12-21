import paho.mqtt.client as mqtt

# MQTT broker details
broker_address = "mqtt.eclipse.org"
broker_address = "broker.hivemq.com"
port = 1883
topic = "iot/virtual_device"

# Callbacks
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")
        # Subscribe to the topic when connected
        client.subscribe(topic)
    else:
        print("Connection failed with code", rc)

def on_message(client, userdata, msg):
    # Callback triggered when a message is received
    payload_str = msg.payload.decode('utf-8')
    print(f"Received message: {payload_str}")

# Create MQTT client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Connect to the broker
client.connect(broker_address, port, 60)

# Keep the script running to receive messages
try:
    client.loop_forever()

except KeyboardInterrupt:
    print("Script terminated by user")
    client.disconnect()
