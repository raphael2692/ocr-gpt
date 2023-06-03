from pydantic import BaseModel

class EncodedImage(BaseModel):
    data : str