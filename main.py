from  fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import EncodedImage, FullProcessResponse

from _ocr import extract_text, decode_image, encode_image
from _ocr.utils import download_image, read_image
from _langchain import answer_quiz, answer_ocr
from _langchain.templates import LONG_ANSWER, SHORT_ANSWER, LETTER_ANSWER, OCR_PROMPT

global TEMPLATES

TEMPLATES = {
    
    'LONG_ANSWER' : LONG_ANSWER,
    'OCR_PROMPT' : OCR_PROMPT
}



import os

app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/process_extract_text")
async def process_extract_text(encoded_image: EncodedImage) -> str:
    image = decode_image(encoded_image.data)
    return extract_text(image)

@app.post("/process_answer_quiz")
async def process_answer_quiz(text: str) -> str:
    return answer_quiz(text)

@app.post("/process_extract_and_predict")
async def process_extract_and_predict(encoded_image: EncodedImage) -> str:
    image = decode_image(encoded_image.data)
    
    text = extract_text(image)
    
    if len(text) < 5:
        raise HTTPException(501, "Can't extract any text")
    return answer_quiz(text)


@app.post("/process_on_clik")
async def process_on_clik_ip_camera(template:str='LONG_ANSWER', screen_url:str|None = None, user_prompt:str|None = None) -> FullProcessResponse:
    
    global TEMPLATES
    
    parent = parent = os.path.dirname(os.path.realpath(__file__))
    download_path = os.path.join(parent, 'download', 'download.jpg')
    
    try:
        download_image('http://192.168.1.146:8090/photo.jpg', download_path)
    except Exception as e:
        print(e)
    
    image = read_image(download_path)
    text = extract_text(image)
    answer = answer_quiz(text, template=TEMPLATES[template])
    response = FullProcessResponse(answer = answer, extracted_text = text)
    print(response)
    return response



@app.post("/process_custom_on_clik")
async def process_custom_on_clik_ip_camera(template:str='OCR_PROMPT', screen_url:str|None = None, user_prompt:str|None = "Explain provided code") -> FullProcessResponse:
    
    global TEMPLATES
    
    parent = parent = os.path.dirname(os.path.realpath(__file__))
    download_path = os.path.join(parent, 'download', 'download_custom.jpg')
    
    try:
        download_image(screen_url, download_path)
    except Exception as e:
        print(e)
    
    image = read_image(download_path)
    text = extract_text(image)
    answer = answer_ocr(text, user_prompt, template=TEMPLATES[template])
    response = FullProcessResponse(answer = answer, extracted_text = text)
    
    print(response)
    
    
    save_prompt = os.path.join(parent, 'results', 'prompt.txt')
    with open(save_prompt, "w") as file:
        file.write(response.answer)
        
    save_code_output = os.path.join(parent, 'results', 'answer.py')
    with open(save_code_output, "w") as file:
        file.write(response.answer)

    save_ocr = os.path.join(parent, 'results', 'ocr.txt')
    with open(save_ocr, "w") as file:
        file.write(response.extracted_text)
    
    return response


