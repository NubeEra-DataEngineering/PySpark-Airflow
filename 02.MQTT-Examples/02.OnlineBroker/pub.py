#pip install paho-mqtt
import time
import random
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
    else:
        print("Connection failed with code", rc)

def on_publish(client, userdata, mid):
    print("Message published")

# Create MQTT client
client = mqtt.Client()
client.on_connect = on_connect
client.on_publish = on_publish

# Connect to the broker
client.connect(broker_address, port, 60)

# Simulation loop
try:
    while True:
        # Simulate sensor data (replace this with your actual data generation logic)
        temperature = random.uniform(20.0, 30.0)
        humidity = random.uniform(40.0, 60.0)

        # Create JSON payload
        payload = {
            "temperature": temperature,
            "humidity": humidity
        }

        # Convert payload to JSON string
        payload_str = str(payload)

        # Publish data to the topic
        client.publish(topic, payload_str)

        # Print the published data
        print(f"Published: {payload_str}")

        # Wait for a moment before publishing the next data
        time.sleep(5)

except KeyboardInterrupt:
    print("Script terminated by user")
    client.disconnect()
