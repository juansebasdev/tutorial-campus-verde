import random
from paho.mqtt import client as mqtt_client
from config.index import config

###////////////////////////////////////////////#
'''
    DEFINE CALLBACKS TO RECEIVE DATA
'''


#////////////////////////////////////////////###


# Generate a random client ID
client_id = f'python-mqtt-{random.randint(0, 10000)}'
# Create a new MQTT client instance
client = mqtt_client.Client(client_id=client_id)
# Set credentials for connection
client.username_pw_set(
    username=config["USER"],
    password=config["PSSWD"]
)

# Start Connection
client.connect(config["HOST"], int(config["PORT"]), keepalive=60)

# Setup Callbacks
client.on_connect = on_connect  # Attach the on_connect function to the client
client.on_message = on_message  # Attach the on_message function to the client

# Start MQTT Client loop
client.loop_forever()
