import random
import json
import time
from paho.mqtt import client as mqtt_client
from config.index import config

###////////////////////////////////////////////#
'''
    DEFINE MQTT CLIENT TO SEND DATA
'''

# Generate a random client ID
client_id = f'python-mqtt-{random.randint(0, 10000)}'
# Create a new MQTT client instance
client = mqtt_client.Client(client_id=client_id)
# Set credentials for connection
# client.username_pw_set(
#     username = config["USER"],
#     password = config["PSSWD"]
# )

# Create Data
data = json.dumps({
    "macAddress": "303E4645",
    "payload": {
        "Fase1": {
            "voltage": 120,
            "current": 5,
        },
        "Fase2": {
            "voltage": 120,
            "current": 5,
        },
        "Fase3": {
            "voltage": 120,
            "current": 5,
        }
    } 
})
# Start Connection
client.connect(config["HOST"], int(config["PORT"]), keepalive=60)
# Send Data
client.publish('rtu/electricMeter', data)

time.sleep(5)
client.disconnect()

#////////////////////////////////////////////###