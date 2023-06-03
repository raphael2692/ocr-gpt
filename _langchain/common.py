import json
import os

parent = os.path.dirname(os.path.realpath(__file__))

def set_env():
    with open(os.path.join(parent, "secrets.json"), "r") as jsonfile:
        secrets = json.load(jsonfile)
    os.environ["OPENAI_API_KEY"] = secrets["openai_key"]