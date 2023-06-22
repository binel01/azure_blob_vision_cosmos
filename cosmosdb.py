import os
import sys
from random import randint

import pymongo




# Récupération de la chaîne de connection
CONNECTION_STRING = os.environ["COSMOS_CONNECTION_STRING"]
# Nom de la base de données
DB_NAME = "azcogimagedescdb1"
# Nom de la collection
COLLECTION_NAME = "desciptions"


# Récupération du client
client = pymongo.MongoClient(CONNECTION_STRING)

# Obtenir la base de données
db = client[DB_NAME]
if DB_NAME not in client.list_database_names():
    db.command({"customAction": "CreateDatabase", "offerThroughput": 400})
    print("Created database '{}' with shared throughput".format(DB_NAME))
else:
    print("Using database: '{}'".format(DB_NAME))

# Create collection if it doesn't exist
collection = db[COLLECTION_NAME]
if COLLECTION_NAME not in db.list_collection_names():
    # Création de la collection si elle n'existe pas
    db.command({"customAction": "CreateCollection", collection: COLLECTION_NAME})
    print("Created collection '{}'".format(COLLECTION_NAME))
else:
    print("Using collection '{}'".format(COLLECTION_NAME))

# Create new document and upsert (insert or update) to collection
image = {
    "url": "image-url",
    "description": "",
    "precision": 0.1
}

result = collection.update_one({"url": image["url"]}, {"$set": image}, upsert=True)
print("Upserted document with id: {}".format(result.upserted_id))









