"""
This is a test file and it is used to test the connection to the MongoDB database.
* After creating a mongo DB container, you can run this file to test the connection to the mongo DB.
* This file will insert a record in the users collection of the profile database.

Create a docker test network:
docker network create testnet

To Spawn a mongo DB latest container:
docker run -d -p 27017:27017 -e MONGO_INITDB_ROOT_USERNAME=admin -e MONGO_INITDB_ROOT_PASSWORD=apollo13 --net testnet --name mongo mongo

Also, I have spawned up a mongo-express container to view the data in the mongo DB.

docker run -d -p 8081:8081 -e ME_CONFIG_MONGODB_ADMINUSERNAME=admin -e ME_CONFIG_MONGODB_ADMINPASSWORD=apollo13 -e ME_CONFIG_MONGODB_SERVER=mongo --net testnet --name mongo-express mongo-express

"""

from pymongo import MongoClient
import uuid

# MongoDB connection string
mongo_uri = "mongodb://admin:apollo13@localhost:27017/"
uid = uuid.uuid4()
contacts = {"userid":str(uid), "name": "John Doe", "address": "USA", "company": "ABCL" }

try:
    # Attempt to connect to MongoDB
    client = MongoClient(mongo_uri)
    db = client.profile  # Replace 'test_database' with your database name
    collection = db.users  # Replace 'test_collection' with your collection name
    
    # Check if the connection is successful
    if client.server_info():
        print("Connection to MongoDB successful!")
        # Now you can perform operations on the MongoDB database
        # For example, you can insert documents, query data, etc.
    else:
        print("Failed to connect to MongoDB.")
    
    print("Attempting to insert values in mongo DB collection users ")
    if collection.update_one({'userid': contacts['userid']}, {'$set':contacts}, upsert=True):
        print("Successfully inserted values in mongo DB collection users ")
    else:
        print("Failed to insert values in mongo DB collection users ")
except Exception as e:
    print("Error:", e)