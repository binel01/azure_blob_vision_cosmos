import os
from azure.storage.blob import BlobServiceClient, ContainerClient

#AZ_STO_ACC = os.environ["AZ_STO_ACC"]
AZ_STO_CONN_STR = os.getenv("AZ_STO_CONN_STR")
CONTAINER_NAME = "images"

print("\n" + AZ_STO_CONN_STR + "\n")

IMAGES_FOLDER = "./images"
FILE_TO_UPLOAD = "belle_plage.jpg"
UPLAOD_FILE_PATH = os.path.join(IMAGES_FOLDER, FILE_TO_UPLOAD)


# Récupération du client BlobServiceClient
blob_service_client = BlobServiceClient.from_connection_string(AZ_STO_CONN_STR)

# Récupération du conteneur
container_client:ContainerClient = blob_service_client.get_container_client(CONTAINER_NAME)

# Création du client Blob avec le nom du fichier à uploader
blob_client = blob_service_client.get_blob_client(container=container_client, blob=FILE_TO_UPLOAD)

# Upload d'une image sur dans le contenur d'images
try:
    print("===== Upload d'une image dans le conteneur images =====")
    res = None
    with open(file=UPLAOD_FILE_PATH, mode="rb") as data:
        res = blob_client.upload_blob(data)
    
    print(res)
    print("===== Upload du fichier {} réussi".format(FILE_TO_UPLOAD))
except Exception as e:
    print("Echec d'upload du fichier {}".format(FILE_TO_UPLOAD))

