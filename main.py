import os

from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes, ImageDescription
from msrest.authentication import CognitiveServicesCredentials

import pymongo


# Clé de Azure Cognitive Services - Computer Vision
VISION_SUBSCRIPTION_KEY = os.environ["VISION_KEY"]
# Point d'accès à Azure Compute Services - Computer Vision
VISION_ENDPOINT = os.environ["VISION_ENDPOINT"]

# Récupération de la chaîne de connection
CONNECTION_STRING = os.environ["COSMOS_CONNECTION_STRING"]
# Nom de la base de données
DB_NAME = "azcogimagedescdb1"
# Nom de la collection
COLLECTION_NAME = "desciptions"


# Url de l'image à analyser
remote_image_url = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-sample-data-files/master/ComputerVision/Images/landmark.jpg"

"""
===========================================================
 1. Analyse the image sent through URL
===========================================================
"""
# Récupération du client Computer Vsision
print("===== Description de l'image =====")
computer_vision_client = ComputerVisionClient(VISION_ENDPOINT, CognitiveServicesCredentials(VISION_SUBSCRIPTION_KEY))
# Call the API with the remote image url
description:ImageDescription = computer_vision_client.describe_image(remote_image_url)
print("Descriptions in the remote image")
if (len(description.captions) == 0):
    print("No captions detected !!")
else:
    for caption in description.captions:
        print("'{}' with confidence {:.2f}".format(caption.text, caption.confidence))
print("===== Fin de la description de l'image =====")


""" 
===========================================================
 2. Store the image description into Cosmos DB collection
===========================================================
""" 
# Enregsitrement de la description dans Cosmos DB
print("===== Enregistrement de la description dans Cosmos DB =====")
# Récupération du client MongoDB
client = pymongo.MongoClient(CONNECTION_STRING)
# Obtenir la base de données
db = client[DB_NAME]
# Obtenir la collection
collection = db[COLLECTION_NAME]

# Création de l'objet ImageDescription
image_description = {
    "url": remote_image_url,
    "description": description.captions[0].text
}
# Insertion de la description dans la base de données
result = collection.update_one({"url": image_description["url"]}, {"$set": image_description}, upsert=True)
print("Insertion du document (url={}) avec l'id: {}".format(image_description["url"], result.upserted_id))
print("===== Fin de l'insertion du document =====")


