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

import pymongo as PyMongo
from flask import Flask


app = Flask(__name__)

client = PyMongo.MongoClient('localhost', 27017);

db = client.prime_db_test
primes = db.primes


@app.route('/') 
def pymongo_data_display():
	my_data = ""
	for document in primes.find():
		my_data += str(document['Message'])
	return my_data
 
if __name__ == '__main__': 
        app.run()


# https://www.blog.pythonlibrary.org/2017/12/14/flask-101-adding-editing-and-displaying-data/