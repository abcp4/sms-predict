from typing import List

from fastapi import FastAPI
from lime.lime_text import LimeTextExplainer
import pickle

from pydantic import BaseModel

app = FastAPI()

model = pickle.load(open("./models/model.pkl", "rb"))
explainer = LimeTextExplainer(class_names=['blocked', 'ok'])

class SMS(BaseModel):
    text: str


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/predict")
def predict_multiple_sms(data: List[SMS]):
    texts = [sms.text for sms in data]
    return {
        "predictions": model.predict(texts).tolist(),
        "probabilities": model.predict_proba(texts).tolist(),
        "texts": texts,
    }


@app.get("/predict")
def predict_sms(text: str):
    exp = explainer.explain_instance(text, model.predict_proba, num_features=20)
    prob = model.predict_proba([text])[0].tolist()
    predicted = model.predict([text])[0]
    return {
        "predicted": predicted,
        "probabilities": prob,
        "explaination": exp.as_list(),
        "html": exp.as_html()
    }

