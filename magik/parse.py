import numpy as np
# import packages
from PIL import Image
import pytesseract
import argparse
import cv2
import os
import re

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("--image", required=True,
	help="path to input image to be OCR'd")
ap.add_argument("-p", "--preprocess", type=str, default="thresh",
	help="type of preprocessing to be done")
args = vars(ap.parse_args())



# load the example image and convert it to grayscale
image = cv2.imread(args["image"])

gray = image
#gray = gray.resize((500, 500 * height / width), Image.ANTIALIAS)


if args["preprocess"] == "thresh":
	gray = cv2.threshold(gray, 0, 255,
		cv2.THRESH_TOZERO)[1]
 
elif args["preprocess"] == "blur":
	gray = cv2.medianBlur(gray, 3)


kernel = np.array([[0,-3,-3], 
                              [-1, 14,-1],
                              [-2,1,-2]])
gray = cv2.filter2D(gray, -1, kernel)

gray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)
#gray = cv2.threshold(gray, 0, 255,
 #              cv2.THRESH_TOZERO | cv2.THRESH_OTSU)[1]




filename = "{}.jpg".format(os.getpid())
cv2.imwrite(filename, gray)

# load the image as a PIL/Pillow image, apply OCR, and then delete
# the temporary file
text = pytesseract.image_to_string(Image.open(filename), lang="deu")
os.remove(filename)
text = re.sub("[^a-zA-Z]+", " ", text)
print(text)
 
# show the output images
#cv2.imshow("Image", image)
#cv2.imshow("Output", gray)
#cv2.waitKey(0)

from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials


endpoint = os.environ['ACCOUNT_ENDPOINT']
key = os.environ['ACCOUNT_KEY']

# Set credentials
credentials = CognitiveServicesCredentials(key)

# Create client
client = ComputerVisionClient(endpoint, credentials)

url = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Bündnis_90_-_Die_Grünen_Logo.svg/2560px-Bündnis_90_-_Die_Grünen_Logo.svg.png"

image_analysis = client.analyze_image(url,visual_features=[VisualFeatureTypes.tags])

for tag in image_analysis.tags:
    print(tag) 
