# AI_medical_assisstant
An AI-powered Medical Assistant built using FastAPI, Streamlit, and Google Gemini.

The application allows users to enter symptoms and receive AI-generated:

Possible Causes
Home Remedies
Doctor Consultation Advice
Emergency Warning Signs
Medical Disclaimer
Features
✅ FastAPI Backend

✅ Streamlit Frontend

✅ Google Gemini Integration

✅ REST API Development

✅ Prompt Engineering

✅ Real-Time Medical Suggestions

✅ Clean UI

Project Architecture
User ↓ Streamlit UI ↓ FastAPI Backend ↓ Gemini API ↓ AI Response ↓ User

Tech Stack
Frontend
Streamlit
Backend
FastAPI
Uvicorn
AI Model
Gemini 2.5 Flash
Libraries
Requests
Python Dotenv
Folder Structure
ai_medical_assistant

├── backend │ └── app.py

├── frontend │ └── streamlit_app.py

├── .env

├── requirements.txt

├── README.md

└── PROJECT_EXPLANATION.md

Installation
Clone Project
git clone

cd ai_medical_assistant

Create Virtual Environment
Mac/Linux

python3 -m venv venv

source venv/bin/activate

Install Dependencies
pip install -r requirements.txt

Configure Environment Variables
Create .env file

GEMINI_API_KEY=YOUR_API_KEY

Run Backend
cd backend

uvicorn app:app --reload

Backend URL

http://127.0.0.1:8000

Swagger Documentation

http://127.0.0.1:8000/docs

Run Frontend
Open another terminal

cd frontend

streamlit run streamlit_app.py

Example Input
I have fever, headache and body pains

Example Output
Possible Causes

Viral Fever
Influenza
Common Infection
Home Remedies

Drink Water
Rest Properly
Consult Doctor

If symptoms persist more than 3 days
Emergency Warning Signs

Breathing difficulty
Disclaimer

This is not a medical diagnosis.
API Endpoint
POST

/medical-assistant

Request

{ "symptoms":"fever and headache" }

Response

{ "response":"AI generated medical advice" }

Future Improvements
Voice Input
Text To Speech
PDF Report Download
Chat History
Medical Knowledge Base
Disease Prediction Models
LangGraph Multi-Agent System
RAG Medical Search
Disclaimer
This project is for educational purposes only.

The generated responses are not medical diagnoses.

Always consult qualified healthcare professionals for medical advice.
