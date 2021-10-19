import classifier as clf
from fastapi import FastAPI
from joblib import load
from iris import Iris

app = FastAPI(title="Iris ML API", description="API for iris dataset ml model", version="1.0")


@app.on_event('startup')
def load_model():
    clf.model = load('predmodel.joblib')

@app.get("/")
def home():
    return {"Hello": "FastAPI Iris ML Ready!"}

@app.post('/predict', tags=["predictions"])
async def get_prediction(iris: Iris):
    data = dict(iris)['data']
    prediction = clf.model.predict(data).tolist()
    log_proba = clf.model.predict_log_proba(data).tolist()
    return {"prediction": prediction,
            "log_proba": log_proba}