from easyocr import Reader
import cv2
from typing import Protocol
import base64
import numpy as np
from .utils import download_image, read_image

def cleanup_text(text):
	# strip out non-ASCII text so we can draw the text on the image
	return "".join([c if ord(c) < 128 else "" for c in text]).strip()

def decode_image_from_txt(txt_path:str):
    with open(txt_path, 'r') as f:
        encoded_img = f.read()
    # Decode the base64-encoded image to bytes
    decoded_img = base64.b64decode(encoded_img)
    # Convert the bytes to a NumPy array
    np_arr = np.frombuffer(decoded_img, dtype=np.uint8)
    # Decode the NumPy array using OpenCV
    return cv2.imdecode(np_arr, flags=cv2.IMREAD_COLOR)


def decode_image(encoded_img:str):
    # Decode the base64-encoded image to bytes
    decoded_img = base64.b64decode(str(encoded_img))
    # Convert the bytes to a NumPy array
    np_arr = np.frombuffer(decoded_img, dtype=np.uint8)
    # Decode the NumPy array using OpenCV
    return cv2.imdecode(np_arr, flags=cv2.IMREAD_COLOR)

def encode_image(image):
    # Convert the image to a byte array using OpenCV
    _ , img_bytes = cv2.imencode('.png', image)
    # Encode the bytes to base64 string
    encoded_img = base64.b64encode(img_bytes).decode('utf-8')
    return encoded_img

def extract_text(opencv_image, cutoff=0.2, langs=['en'], gpu=False):

    reader = Reader(langs, gpu)
    results = reader.readtext(opencv_image)
    
    texts = []
    
    for (_, text, prob) in results:
        # display the OCR'd text and associated probability
        if prob > cutoff:
            texts.append(cleanup_text(text))

    return (" \n".join(texts))
       

# TEST
# image = decode_image_from_txt('C:\\dev\\easy-ocr-api\\base64.txt')
# print(extract_text(image))

