from fastapi import FastAPI

app = FastAPI()

# Home Page
@app.get("/")
def home():
    return {"message": "AI Medical Assistant API Running"}

# Medical Advice
@app.get("/advice/{symptom}")
def advice(symptom: str):

    if symptom == "fever":
        return {"advice": "Drink water, take rest, and monitor your temperature."}

    elif symptom == "cold":
        return {"advice": "Stay hydrated and get enough sleep."}

    elif symptom == "headache":
        return {"advice": "Rest in a quiet room and drink water."}

    else:
        return {"advice": "Please consult a doctor for proper guidance."}