import requests
import sys
# If you are using a Jupyter notebook, uncomment the following line.
#%matplotlib inline
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from PIL import Image
from io import BytesIO

def parsing(name):
   # Replace <Subscription Key> with your valid subscription key.
   subscription_key = "1400d870a7c24ab599b8d0b4a5e0e3d2"
   assert subscription_key

# You must use the same region in your REST call as you used to get your
# subscription keys. For example, if you got your subscription keys from
# westus, replace "westcentralus" in the URI below with "westus".
#
# Free trial subscription keys are generated in the "westus" region.
# If you use a free trial subscription key, you shouldn't need to change
# this region.
   vision_base_url = "https://westeurope.api.cognitive.microsoft.com/vision/v2.0/"

   ocr_url = vision_base_url + "ocr"

# Set image_url to the URL of an image that you want to analyze.
   image_url = "https://raw.githubusercontent.com/guessthepartei/App/master/magik/dataset/" + name


   headers = {'Ocp-Apim-Subscription-Key': subscription_key}
   params  = {'language': 'de', 'detectOrientation': 'true'}
   data    = {'url': image_url}
   response = requests.post(ocr_url, headers=headers, params=params, json=data)
   response.raise_for_status()

   analysis = response.json()

# Extract the word bounding boxes and text.
   line_infos = [region["lines"] for region in analysis["regions"]]
   word_infos = []
   lines = []
   str = ""
   for line in line_infos:
      for word_metadata in line:
         for word_info in word_metadata["words"]:
            str = str + " " + word_info["text"]
      str = str + "\n"
   word_infos
   print(str)
   return str
