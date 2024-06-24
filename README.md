# Pi-MQTT
MQTT Framwork for Raspberry Pi using Mosquitto, intended to be used/built upon for future IOT projects.

# v0.0.1
This version allows for basic communication between the Pi client and the PC client, using the broker. The Pi connects to the broker and publishes the currently measured temperature to the subscription "temperature", in which the PC client subscribes to and then reads and prints the temperature value to the console.
