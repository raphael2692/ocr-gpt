import requests
import os
import cv2

def download_image(url: str, file_path: str) -> bool:
    try: 
        response = requests.get(url)
        with open(file_path, "wb") as f:
            f.write(response.content)
        return True
    except Exception as e:
        print(e)
        return False
    
def read_image(file_path: str):
    return cv2.imread(file_path)
    

# test

# base_path = 'C:\\dev\\easy-ocr-api\\download'
# url = 'http://192.168.1.146:8090/photo.jpg'
# file_name = url.split('/')[-1]
# file_path = os.path.join(base_path, file_name)

# download_image(url, file_path)
