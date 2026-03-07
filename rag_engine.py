import json
import os

DATA_PATH = os.path.join("data", "schemes.json")

with open(DATA_PATH, "r", encoding="utf-8") as f:
    schemes = json.load(f)

def search(query):

    query = query.lower()

    for scheme in schemes:
        if scheme["name"].lower() in query:
            return scheme

    return schemes[0]