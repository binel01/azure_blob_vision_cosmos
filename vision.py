from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes, ImageDescription

from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image
import sys
import time

#Authenticate
"""
Authenticates your credentials and creates a client
"""
subscription_key = os.environ["VISION_KEY"]
endpoint = os.environ["VISION_ENDPOINT"]

computer_vision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))
# End Authenticate

# Quickstart variables
"""
These variables are shared by several examples
Images used for the examples: Decsribe an image, categorize an image, Tag an image,
Detect faces, Detect adult or racy content, Detect the color scheme, 
Detect domain-specific content, Detect image types, Detect objects
"""
images_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")
remote_image_url = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-sample-data-files/master/ComputerVision/Images/landmark.jpg"
# End Quickstart

# Tag an Image - Remote
print("===== Tag an image - Remote =====")
# Call API with remote Image URL
tags_result_remote = computer_vision_client.tag_image(remote_image_url)

# Print results with confidence score
print("Tags in the remote image")
if (len(tags_result_remote.tags) == 0):
    print("No tags detected !!")
else:
    for tag in tags_result_remote.tags:
        print("'{}' with confidence {:.2f}".format(tag.name, tag.confidence))
print()
# End - Tag an Image Remote
print("End of Computer Vision Quick Start !!")



# Describe an image - Remote
print("===== Describe and image -Remote =====")
# Call the API with the remote image url
description:ImageDescription = computer_vision_client.describe_image(remote_image_url)

# Print the description of the image
print("Descriptions in the remote image")
if (len(description.captions) == 0):
    print("No captions detected !!")
else:
    for caption in description.captions:
        print("--> '{}' with confidence {:.2f}".format(caption.text, caption.confidence))
print()
# End - Tag an Image Remote
print("End of Computer Vision Quick Start !!")

