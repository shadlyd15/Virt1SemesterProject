#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2010-2013 Roger Light <roger@atchoo.org>
#
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Eclipse Distribution License v1.0
# which accompanies this distribution.
#
# The Eclipse Distribution License is available at
#   http://www.eclipse.org/org/documents/edl-v10.php.
#
# Contributors:
#    Roger Light - initial implementation
# Copyright (c) 2010,2011 Roger Light <roger@atchoo.org>
# All rights reserved.

# This shows a simple example of an MQTT subscriber.

# import context  # Ensures paho is in PYTHONPATH
import paho.mqtt.client as mqtt
import pymongo as PyMongo

client = PyMongo.MongoClient('localhost', 27017);

db = client.prime_db_test
primes = db.primes

def print_primes():
	for document in primes.find():
		if 'TP' in document:
			print document['TP']

def on_connect(mqttc, obj, flags, rc):
    print("MQTT Client Connected")

def on_message(mqttc, obj, msg):
	# nonlocal primes
	print(msg.topic + " : " + str(msg.payload))
	result = primes.insert_one({'Topic': msg.topic, 'TP':msg.payload})
	# print('One post: {0}'.format(result.inserted_id))
	print_primes()

def on_subscribe(mqttc, obj, mid, granted_qos):
	print("Subscribed")

mqttc = mqtt.Client()
mqttc.on_message = on_message
mqttc.on_connect = on_connect

mqttc.connect("localhost", 1883, 60)
mqttc.subscribe("TEST", 0)



mqttc.loop_forever()