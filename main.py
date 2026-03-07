from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from ai_engine import generate_response

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "SetuAI running"}

@app.get("/ask")
def ask(query: str, lang: str = "auto"):

    result = generate_response(query, lang)

    return result

@app.get("/eligibility")
def eligibility(income:int):

    if income < 300000:
        return {"result":"Eligible for many government welfare schemes"}
    elif income < 800000:
        return {"result":"Eligible for some government schemes"}
    else:
        return {"result":"May not qualify for income based schemes"}