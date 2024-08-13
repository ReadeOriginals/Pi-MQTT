# Pi-MQTT
MQTT Framwork for Raspberry Pi and Pi Pico using Mosquitto, intended to be used/built upon for future IOT projects.
See "Releases" for the different versions of the code developed.

# v0.1.0
This version allows for basic communication between the Pi client and the PC client, using the broker. The Pi connects to the broker and publishes the currently measured temperature to the subscription "temperature", in which the PC client subscribes to and then reads and prints the temperature value to the console. It is inefficient due to the use of threading.

# v1.1.0
This version allows for a Pi Pico to send the temperature of the Pico CPU to a PC client using MQTT. The Pico connects to the broker and publishes the currently measured temperature to the subscription "temperature", in which the PC client subscribes to and then reads and prints the temperature value to the console. Callback messages on connection and on message recieved have been included. Threading has been removed for simpler running.
