from pydantic import BaseModel

class Template(BaseModel):
    text: str
    input_variables: list