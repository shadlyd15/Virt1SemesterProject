#!/usr/bin/python

import paho.mqtt.client as mqtt
import pymongo as PyMongo

pyMongoClient = PyMongo.MongoClient('localhost', 27017);

dbClient = pyMongoClient.prime_db_test
primes = dbClient.primes

def print_primes():
	count = 0
	for document in primes.find():
		if all (k in document for k in ("TPrime","TimeStamp")):
			print("Prime : " + str(document['TPrime']) + ", TimeStamp : " + str(document['TimeStamp']))
			count += 1
	print("Total " + str(count) + " Entries Found in Database\r\n")

def on_connect(mqttClient, obj, flags, rc):
    mqttClient.connected = True
    print("MQTT Client Connected")

def on_disconnect(mqttClient, userdata, rc):
    mqttClient.connected = False
    mqttClient.loop_stop()
    print("MQTT Client Disonnected")

def on_subscribe(mqttClient, obj, mid, granted_qos):
	print("Subscribed")

def nth_prime_number(n):
    if n==1:
        return 2
    count = 1
    num = 1
    while(count < n):
        num +=2 #optimization
        if is_prime(num):
            count +=1
    return num

def is_prime(num):
    factor = 2
    while (factor * factor <= num):
        if num % factor == 0:
             return False
        factor +=1
    return True


mqttClient = mqtt.Client()
mqttClient.connected = False
mqttClient.on_connect = on_connect
mqttClient.on_disconnect = on_disconnect

mqttClient.connect("localhost", 1883, 10)
mqttClient.loop_start()

prime_count = 1
while True:
	if mqttClient.connected == True:
		option = input("""
Press 's' to print primes from database
Press 'p' to publish new prime to mqtt broker
Press 'q' to quit
Input :	""")

		if option.lower() == 's' :
			print_primes()
		elif option.lower() == 'p' :
			prime = nth_prime_number(prime_count)
			print("Publishing " + str(prime_count) + "th Prime " + str(prime) + " : { " + "Prime : " + str(prime) + " }")
			mqttClient.publish("Prime", str(prime))
			prime_count += 1
		elif option.lower() == 'q' :
			print("Quiting...")
			break
		else :
			print("Invalid Option")
