from pydantic import BaseModel

class EncodedImage(BaseModel):
    data : str
    
class FullProcessResponse(BaseModel):
    
    answer: str
    extracted_text : str