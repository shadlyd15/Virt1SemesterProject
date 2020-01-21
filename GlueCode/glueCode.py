#!/usr/bin/python

import paho.mqtt.client as mqtt
import pymongo as PyMongo

from datetime import datetime

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
    print("MQTT Client Connected")

def on_message(mqttClient, obj, msg):
	print("New Prime Received")
	print(msg.topic + " : " + str(msg.payload) + " TimeStamp : " + datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
	result = primes.insert_one({'TPrime':msg.payload, 'TimeStamp':datetime.now().strftime("%m/%d/%Y, %H:%M:%S")})
	print('Inserted Id : {0}'.format(result.inserted_id))

def on_subscribe(mqttClient, obj, mid, granted_qos):
	print("Subscribed")

mqttClient = mqtt.Client()
mqttClient.on_message = on_message
mqttClient.on_connect = on_connect

mqttClient.connect("localhost", 1883, 60)
mqttClient.subscribe("Prime", 0)

mqttClient.loop_forever()