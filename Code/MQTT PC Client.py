import paho.mqtt.client as mqtt

# Server Details
serverIP = "192.168.100.175"
serverPort = 1883

# MQTT client instance
client = mqtt.Client(client_id="BrandonDesktop")

# Seting up MQTT client
client.username_pw_set("Hobbs","RobbieFowler123")
client.connect(serverIP, serverPort, 60)

# Subscribe to the "temperature" topic
client.subscribe("temperature")

# Callback function for connection
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")
    else:
        print("Failed to connect to the MQTT broker, return code: ", rc)

# Callback function to handle incoming messages
def on_message(client, userdata, message):
    print("Received message:", message.payload.decode())

# on_connect & on_message callback
client.on_connect = on_connect
client.on_message = on_message

# Loop forever to receive messages
client.loop_forever()