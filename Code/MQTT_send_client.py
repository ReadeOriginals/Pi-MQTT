import paho.mqtt.client as mqtt
import time
from gpiozero import CPUTemperature
import threading

# Server Details
serverIP = "192.168.100.175"
serverPort = 1883

# Seting up MQTT client
client = mqtt.Client(client_id="Pi400")
client.username_pw_set("Hobbs","RobbieFowler123")
client.connect(serverIP, serverPort, 60)
client.subscribe("temperature")

# Defining the on_connect callback
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")
    else:
        print("Failed to connect to the MQTT broker, return code: ", rc)


# Defining the on_messge callback
def on_message(client, userdata, message):
    print(f"Received message on topic {message.topic}: {message.payload.decode()}")

# on_connect & on_message callback
client.on_connect = on_connect
client.on_message = on_message

# start loop
client.loop_start()

# Function to read CPU Temp
def check_CPU_temp():
    temp = CPUTemperature()
    print("Measured temperature: " + str(temp.temperature))
    return temp.temperature

def publish_temp(client):
    while True:
        # Getting temp
        str_temp = str(check_CPU_temp())
        
        # Publishing temp
        try:
            client.publish("temperature", str_temp, qos=0)

        except Exception as e:
            print(f"Error publishing message: {e}")
            
        time.sleep(2)
        

# Thread to publish temperature data
thread = threading.Thread(target=publish_temp, args=(client,))
print("Thread created")
thread.daemon = True # Set daemon thread so it exists when main thread exists
thread.start()

while True:
    # Keep main thread running to prevent it from exiting
    time.sleep(1)
