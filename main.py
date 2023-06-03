from  fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import EncodedImage

from _ocr import extract_text, decode_image, encode_image

app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/extract_text")
async def extract_text(encoded_image: EncodedImage) -> str:
    image = decode_image(encoded_image.data)
    return extract_text(image)
